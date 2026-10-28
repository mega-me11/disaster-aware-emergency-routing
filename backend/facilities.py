
from backend.algorithms import dijkstra


def find_nearest_facility(graph, start, facilities):
    """Find the closest reachable facility by travel time.

    facilities is a dictionary such as:
    {
        "City Hospital": "C",
        "Relief Shelter": "F"
    }
    """

    if start not in graph.adjacency:
        raise ValueError(f"Unknown location: {start}")

    if not facilities:
        return None

    best_facility = None
    best_path = None
    best_time = float("inf")

    for facility_name, facility_location in facilities.items():
        if facility_location not in graph.adjacency:
            continue

        path, travel_time = dijkstra(
            graph,
            start,
            facility_location,
            weight="travel_time_min",
        )

        if path is not None and travel_time < best_time:
            best_facility = facility_name
            best_path = path
            best_time = travel_time

    if best_facility is None:
        return None

    return {
        "facility": best_facility,
        "location": best_path[-1],
        "path": best_path,
        "travel_time_min": best_time,
        "message": "Nearest reachable facility found.",
    }
