
const API_BASE = "https://ubiquitous-parakeet-r4j4rrjxgjprcpg56-8000.app.github.dev";

const start = document.getElementById("start");
const destination = document.getElementById("destination");
const result = document.getElementById("result");

const roadStart = document.getElementById("roadStart");
const roadEnd = document.getElementById("roadEnd");
const statusSelect = document.getElementById("status");

let selectedMode = "fastest";

async function loadLocations() {
    try {
        const response = await fetch(`${API_BASE}/locations`);

        if (!response.ok) {
            throw new Error("Could not load locations.");
        }

        const data = await response.json();

        [start, destination, roadStart, roadEnd].forEach(select => {
            const previousValue = select.value;

            select.replaceChildren(
                new Option(
                    select === start ? "Select Source" :
                    select === destination ? "Select Destination" :
                    select === roadStart ? "Select first location" :
                    "Select second location",
                    ""
                )
            );

            data.locations.forEach(location => {
                select.add(new Option(`Location ${location}`, location));
            });

            select.value = previousValue;
        });
    } catch (error) {
        result.textContent =
            "Could not connect to the backend. Check the API URL and ensure the server is running.\n" +
            error.message;
    }
}

async function findRoute(preference = selectedMode) {
    selectedMode = preference;

    const source = start.value;
    const target = destination.value;

    if (!source || !target) {
        result.textContent = "Please select both source and destination.";
        return;
    }

    if (source === target) {
        result.textContent = "Source and destination must be different.";
        return;
    }

    result.textContent = "Calculating route...";

    try {
        const params = new URLSearchParams({
            start: source,
            destination: target,
            preference: selectedMode
        });

        const response = await fetch(`${API_BASE}/route?${params}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Route calculation failed.");
        }

        if (!data.path || data.path.length === 0) {
            result.textContent = data.message || "No route available.";
            return;
        }

        result.textContent =
            `Preference: ${data.preference}\n` +
            `Route: ${data.path.join(" → ")}\n` +
            `Distance: ${data.total_distance_km} km\n` +
            `Travel time: ${data.total_travel_time_min} minutes\n` +
            `Risk score: ${data.total_risk}\n` +
            `Optimization cost: ${data.optimization_cost}\n` +
            `${data.message || "Route found successfully."}`;
    } catch (error) {
        result.textContent = `Error: ${error.message}`;
    }
}

document.getElementById("fastest").addEventListener("click", () => {
    findRoute("fastest");
});

document.getElementById("safest").addEventListener("click", () => {
    findRoute("safest");
});

document.getElementById("shortest").addEventListener("click", () => {
    findRoute("shortest");
});

document.getElementById("updateRoad").addEventListener("click", async () => {
    const location1 = roadStart.value;
    const location2 = roadEnd.value;
    const status = statusSelect.value;

    if (!location1 || !location2) {
        result.textContent = "Please select both ends of the road.";
        return;
    }

    if (location1 === location2) {
        result.textContent = "Choose two different locations.";
        return;
    }

    result.textContent = "Updating road status...";

    try {
        const response = await fetch(`${API_BASE}/road-status`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                location1,
                location2,
                status
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Road status update failed.");
        }

        result.textContent =
            `Road ${location1} – ${location2} updated to ${status}.\n` +
            `${data.message || JSON.stringify(data)}\n\n` +
            "Click a routing preference to calculate the updated route.";
    } catch (error) {
        result.textContent = `Error: ${error.message}`;
    }
});

loadLocations();
