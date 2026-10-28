
class RoadNetwork:
    """Represent a road network using an adjacency list."""

    def __init__(self):
        self.adjacency = {}

    def add_location(self, location):
        """Add a location to the graph."""
        if location not in self.adjacency:
            self.adjacency[location] = {}

    def add_road(
        self,
        location1,
        location2,
        distance_km,
        travel_time_min,
        risk,
        status="NORMAL",
    ):
        """Add an undirected road between two locations."""

        if distance_km <= 0 or travel_time_min <= 0:
            raise ValueError("Distance and travel time must be positive.")

        if not 1 <= risk <= 10:
            raise ValueError("Risk must be between 1 and 10.")

        allowed_statuses = {
            "NORMAL",
            "RISKY",
            "FLOODED",
            "DAMAGED",
            "BLOCKED",
        }

        if status not in allowed_statuses:
            raise ValueError("Invalid road status.")

        self.add_location(location1)
        self.add_location(location2)

        road = {
            "distance_km": distance_km,
            "travel_time_min": travel_time_min,
            "risk": risk,
            "status": status,
        }

        # Both directions refer to the same road record.
        self.adjacency[location1][location2] = road
        self.adjacency[location2][location1] = road

    def get_neighbors(self, location):
        """Return the neighboring locations and their road data."""
        if location not in self.adjacency:
            raise ValueError(f"Unknown location: {location}")

        return self.adjacency[location]
