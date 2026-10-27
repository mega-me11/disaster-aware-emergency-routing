
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from backend.graph import RoadNetwork
from backend.routing import find_route
from backend.disaster_updates import update_road_status

app = FastAPI(
    title="Disaster-Aware Emergency Routing System",
    description="Graph-based emergency routing with disaster updates.",
    version="1.0.0",
)

# Temporary sample network for development.
# Later, we can replace this with data loaded from a file.
graph = RoadNetwork()

graph.add_road("A", "B", 2.0, 5, 2)
graph.add_road("A", "D", 1.0, 3, 1)
graph.add_road("B", "C", 3.0, 8, 4)
graph.add_road("B", "E", 2.0, 4, 3)
graph.add_road("C", "F", 1.0, 2, 2)
graph.add_road("D", "E", 2.0, 4, 2)
graph.add_road("E", "F", 3.0, 6, 4)


class RoadStatusRequest(BaseModel):
    location1: str
    location2: str
    status: str


@app.get("/")
def home():
    return {"message": "Emergency Routing API is running."}


@app.get("/locations")
def get_locations():
    return {"locations": sorted(graph.adjacency.keys())}


@app.get("/route")
def get_route(
    start: str,
    destination: str,
    preference: str = "fastest",
):
    try:
        result = find_route(graph, start, destination, preference)
        return result
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.post("/road-status")
def change_road_status(request: RoadStatusRequest):
    try:
        return update_road_status(
            graph,
            request.location1,
            request.location2,
            request.status.upper(),
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
