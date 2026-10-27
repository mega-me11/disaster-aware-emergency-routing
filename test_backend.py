
from backend.facilities import find_nearest_facility
from backend.graph import RoadNetwork
from backend.routing import find_route
from backend.disaster_updates import (
    update_road_status,
    simulate_disaster,
)

town = RoadNetwork()

town.add_road("A", "B", 2.0, 5, 2)
town.add_road("A", "D", 1.0, 3, 1)
town.add_road("B", "C", 3.0, 8, 4)
town.add_road("B", "E", 2.0, 4, 3)
town.add_road("C", "F", 1.0, 2, 2)
town.add_road("D", "E", 2.0, 4, 2)
town.add_road("E", "F", 3.0, 6, 4)

print("BEFORE DISASTER")
print(find_route(town, "A", "F", "fastest"))

print("\nSIMULATING FLOOD ON D-E")
print(simulate_disaster(town, "D", "E", "flood"))

print("\nAFTER DISASTER")
print(find_route(town, "A", "F", "fastest"))

print("\nBLOCKING ROAD B-E")
print(update_road_status(town, "B", "E", "BLOCKED"))

print("\nAFTER ROAD CLOSURE")
print(find_route(town, "A", "F", "fastest"))

print("\nNEAREST FACILITY FROM A")

facilities = {
    "City Hospital": "C",
    "Relief Shelter": "F",
    "Medical Camp": "D",
}

print(find_nearest_facility(town, "A", facilities))
