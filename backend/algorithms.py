#BFS

from collections import deque


def bfs(graph, start):
    """Return nodes in breadth-first traversal order."""

    if start not in graph.adjacency:
        raise ValueError(f"Unknown location: {start}")

    visited = {start}
    queue = deque([start])
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        for neighbor, road in graph.get_neighbors(current).items():
            if road["status"] == "BLOCKED":
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

#DFS

def dfs(graph, start):
    """Return nodes in depth-first traversal order."""

    if start not in graph.adjacency:
        raise ValueError(f"Unknown location: {start}")

    visited = {start}
    stack = [start]
    traversal_order = []

    while stack:
        current = stack.pop()
        traversal_order.append(current)

        # Reverse the neighbors so they are explored
        # in alphabetical order when popped.
        neighbors = sorted(graph.get_neighbors(current).keys(),
                           reverse=True)

        for neighbor in neighbors:
            road = graph.get_neighbors(current)[neighbor]

            if road["status"] == "BLOCKED":
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return traversal_order



import heapq

from collections import deque


STATUS_MULTIPLIERS = {
    "NORMAL": 1.0,
    "RISKY": 1.5,
    "FLOODED": 3.0,
    "DAMAGED": 2.0,
    "BLOCKED": None,
}


def dijkstra(graph, start, destination, weight="travel_time_min"):
    """Find a minimum-cost route while accounting for road conditions."""

    if start not in graph.adjacency:
        raise ValueError(f"Unknown location: {start}")

    if destination not in graph.adjacency:
        raise ValueError(f"Unknown location: {destination}")

    if weight not in {"travel_time_min", "risk", "distance_km"}:
        raise ValueError("Invalid routing weight.")

    distances = {node: float("inf") for node in graph.adjacency}
    previous = {node: None for node in graph.adjacency}

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)

        if current_cost > distances[current]:
            continue

        if current == destination:
            break

        for neighbor, road in graph.get_neighbors(current).items():
            status = road["status"]
            multiplier = STATUS_MULTIPLIERS[status]

            # Never travel along a blocked road.
            if multiplier is None:
                continue

            base_cost = road[weight]

            if weight == "risk":
                edge_cost = base_cost * multiplier
            else:
                edge_cost = base_cost * multiplier

            new_cost = current_cost + edge_cost

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current
                heapq.heappush(priority_queue, (new_cost, neighbor))

    if distances[destination] == float("inf"):
        return None, float("inf")

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[destination]
