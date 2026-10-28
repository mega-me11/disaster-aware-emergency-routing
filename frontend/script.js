const start = document.getElementById("start");
const destination = document.getElementById("destination");
const result = document.getElementById("result");

let selectedMode = "balanced";

document.getElementById("fastest").addEventListener("click", () => {
    selectedMode = "fastest";
    findRoute();
});

document.getElementById("safest").addEventListener("click", () => {
    selectedMode = "safest";
    findRoute();
});

document.getElementById("balanced").addEventListener("click", () => {
    selectedMode = "balanced";
    findRoute();
});

function findRoute() {
    const source = start.value;
    const destinationValue = destination.value;

    if (!source || !destinationValue) {
        result.textContent = "Please select both source and destination.";
        return;
    }

    if (source === destinationValue) {
        result.textContent = "Source and destination must be different.";
        return;
    }

    
    result.textContent =
    "Route Preview\n" +
    "Source: " + source + "\n" +
    "Destination: " + destinationValue + "\n" +
    "Selected mode: " + selectedMode.charAt(0).toUpperCase() + selectedMode.slice(1) + "\n" +
    "This is a frontend preview. Actual route calculation will be connected later.";
}

document.getElementById("updateRoad").addEventListener("click", () => {
    const road = document.getElementById("road").value.trim();
    const status = document.getElementById("status").value;

    if (!road) {
        result.textContent = "Please enter a road name.";
        return;
    }

    result.textContent = "Road: " + road + " | Status: " + status;
});
