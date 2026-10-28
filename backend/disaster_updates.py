
VALID_STATUSES = {
    "NORMAL",
    "RISKY",
    "FLOODED",
    "DAMAGED",
    "BLOCKED",
}


def update_road_status(graph, location1, location2, new_status):
    """Update the status of an existing road."""

    if new_status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status. Choose from: {sorted(VALID_STATUSES)}"
        )

    if location1 not in graph.adjacency:
        raise ValueError(f"Unknown location: {location1}")

    if location2 not in graph.adjacency[location1]:
        raise ValueError(f"No road exists between {location1} and {location2}")

    # Both directions share the same road dictionary.
    road = graph.adjacency[location1][location2]
    road["status"] = new_status

    return {
        "road": [location1, location2],
        "status": new_status,
        "message": f"Road {location1}-{location2} updated to {new_status}.",
    }


def simulate_disaster(graph, location1, location2, disaster_type):
    """Apply a simple simulated disaster to a road."""

    disaster_statuses = {
        "flood": "FLOODED",
        "earthquake": "DAMAGED",
        "fire": "RISKY",
        "landslide": "BLOCKED",
    }

    disaster_type = disaster_type.lower()

    if disaster_type not in disaster_statuses:
        raise ValueError(
            f"Unsupported disaster type: {disaster_type}"
        )

    return update_road_status(
        graph,
        location1,
        location2,
        disaster_statuses[disaster_type],
    )
