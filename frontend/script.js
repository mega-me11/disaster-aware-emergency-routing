document.getElementById("findRoute").addEventListener("click", function () {
const start = document.getElementById("start").value.trim();
const destination = document.getElementById("destination").value.trim();
const vehicle = document.getElementById("vehicle").value;
const result = document.getElementById("result");

if (start === "" || destination === "") {
    result.textContent = "Please enter both starting point and destination.";
    return;
}

if (start.toLowerCase() === destination.toLowerCase()) {
    result.textContent = "Starting point and destination cannot be the same.";
    return;
}

result.innerHTML =
    "<strong>Route Request Received!</strong><br>" +
    "Start: " + start + "<br>" +
    "Destination: " + destination + "<br>" +
    "Emergency Vehicle: " + vehicle + "<br><br>" +
    "Route calculation will be connected to the DSA algorithm next.";

});
