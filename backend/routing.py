
from backend.algorithms import dijkstra


def find_route(graph, start, destination, preference="fastest"):
    """Find a route based on the selected routing preference."""

    weight_options = {
        "fastest": "travel_time_min",
        "safest": "risk",
        "shortest": "distance_km",
    }

    if preference not in weight_options:
        raise ValueError(
            "Preference must be 'fastest', 'safest', or 'shortest'."
        )

    path, cost = dijkstra(
        graph,
        start,
        destination,
        weight_options[preference],
    )

    if path is None:
        return {
            "path": None,
            "preference": preference,
            "total_distance_km": None,
            "total_travel_time_min": None,
            "total_risk": None,
            "message": "No available route between these locations.",
        }

    total_distance = 0
    total_time = 0
    total_risk = 0

    for i in range(len(path) - 1):
        road = graph.get_neighbors(path[i])[path[i + 1]]

        total_distance += road["distance_km"]
        total_time += road["travel_time_min"]
        total_risk += road["risk"]

    return {
        "path": path,
        "preference": preference,
        "total_distance_km": round(total_distance, 2),
        "total_travel_time_min": total_time,
        "total_risk": total_risk,
        "optimization_cost": cost,
        "message": "Route found successfully.",
    }
