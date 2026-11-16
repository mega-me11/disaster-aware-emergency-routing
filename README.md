# Disaster-Aware Emergency Routing System

A graph-based emergency routing system that identifies suitable routes between locations using graph traversal, shortest-path algorithms, and dynamically updated road conditions.

## Overview

During disasters such as floods, earthquakes, fires, and landslides, normal routes may become risky or inaccessible. This project demonstrates how graph algorithms can help identify alternative routes based on road conditions and user-selected routing preferences.

The road network is represented as a weighted graph. Locations are modeled as vertices, while roads are represented as edges containing distance, estimated travel time, risk score, and road status.

The system uses Python and FastAPI to provide route information through API endpoints. A web frontend built with HTML, CSS, and JavaScript is included for user interaction.

## Objectives

- Represent a road network using a graph data structure.
- Implement BFS and DFS for graph traversal.
- Use Dijkstra's algorithm for weighted route selection.
- Support fastest, shortest, and safest routing preferences.
- Update road conditions dynamically.
- Exclude blocked roads from route calculations.
- Recalculate routes when road conditions change.
- Demonstrate how graph algorithms can support emergency-routing decisions.

## Features

- **Graph-based road network:** Locations and roads are represented using an adjacency-list structure.
- **Multiple routing preferences:** Select routes based on travel time, distance, or risk score.
- **Disaster-aware road conditions:** Support NORMAL, RISKY, FLOODED, DAMAGED, and BLOCKED road statuses.
- **Dynamic road updates:** Change road conditions through an API and calculate routes using the updated network.
- **Alternative-route selection:** Find a different available route when a road becomes blocked or less desirable.
- **REST API:** Access locations, request routes, and update road conditions through FastAPI.
- **Facility lookup logic:** The backend includes a function to find a reachable facility based on estimated travel time.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Graph representation | Adjacency list |
| Graph algorithms | BFS, DFS, Dijkstra's algorithm |
| Backend framework | FastAPI |
| Request validation | Pydantic |
| Frontend | HTML, CSS, JavaScript |
| Version control | Git and GitHub |

## Project Structure

```text
disaster-aware-emergency-routing/
├── backend/
│   ├── __init__.py
│   ├── graph.py
│   ├── algorithms.py
│   ├── routing.py
│   ├── disaster_updates.py
│   ├── facilities.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── requirements.txt
├── README.md
└── test_backend.py
```

*The structure above reflects the current backend layout. Update it if files have been added, renamed, or removed.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mega-me11/disaster-aware-emergency-routing.git
cd disaster-aware-emergency-routing
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the backend server

Run the following command from the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will be available at:

- API root: http://127.0.0.1:8000/
- Interactive API documentation: http://127.0.0.1:8000/docs
- Alternative API documentation: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check whether the API is running |
| GET | `/locations` | Retrieve available locations |
| GET | `/route` | Calculate a route between two locations |
| POST | `/road-status` | Update the status of a road |

### Example: Request a route

```http
GET /route?start=A&destination=F&preference=fastest
```

Example request URL when running locally:

```text
http://127.0.0.1:8000/route?start=A&destination=F&preference=fastest
```

Supported routing preferences:

- `fastest` — minimize the adjusted travel-time cost.
- `shortest` — minimize the adjusted distance cost.
- `safest` — minimize the adjusted risk cost.

### Example: Update a road condition

Send a POST request to `/road-status` with a JSON body:

```json
{
  "location1": "D",
  "location2": "E",
  "status": "FLOODED"
}
```

Supported statuses are `NORMAL`, `RISKY`, `FLOODED`, `DAMAGED`, and `BLOCKED`.

## How It Works

1. The road network is initialized as a weighted graph.
2. The user selects a source, destination, and routing preference.
3. The backend evaluates reachable roads and their weights.
4. Dijkstra's algorithm determines a route with the lowest adjusted cost for the selected preference.
5. Blocked roads are excluded from route calculations.
6. The selected route and its details are returned by the API.
7. When a road status changes, subsequent route requests use the updated network.

BFS and DFS are used for graph traversal, while Dijkstra's algorithm is used for weighted route selection.

## Testing

The backend has been tested using a sample network with locations A–F.

| Scenario | Expected demonstration |
|---|---|
| Normal road conditions | Find a route from A to F |
| Road D–E becomes FLOODED | Recalculate the route using updated road costs |
| Road B–E becomes BLOCKED | Exclude B–E and find an alternative if one exists |
| Facility lookup from A | Identify the reachable facility with the lowest estimated travel time |

Actual outputs depend on the network configuration and current road statuses. Add screenshots of the tested API responses and the integrated frontend before final submission.

## Limitations

- Uses a predefined sample road network rather than a live geographic map.
- Disaster conditions are updated manually through the API.
- Risk scores and road-condition penalties are illustrative, not calibrated real-world safety predictions.
- Does not currently incorporate live traffic, weather feeds, GPS tracking, or facility capacity.
- A calculated route should not be treated as verified emergency guidance.

## Future Scope

- Integrate geographic maps and real road-network data.
- Incorporate live traffic and weather information.
- Add persistent storage for road conditions and locations.
- Extend facility lookup and emergency-service information.
- Improve risk estimation using validated data.
- Add route history and more advanced visualization.

## Contributors

- Megha Chatterjee — Backend, graph algorithms, API integrations, Presentation
- Samadrita Dey — Frontend development, Presentation 
- Shreya Bera — Frontend development
- Tisya Chakraborty - Report Documentation 



## Academic Project

Developed as a Data Structures and Algorithms project to demonstrate graph representation, traversal, shortest-path algorithms, and dynamic route recalculation.
