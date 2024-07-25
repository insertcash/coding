// quick log test
console.log("log1");
let data;

// acquire data from api, then convert to json for actually usable stuff
document.getElementById("loc-submit").addEventListener("click", function () {
  // getting location to fetch data for, and combining it with api to create link
  let fetchstr =
    "https://api.weatherapi.com/v1/current.json?key=57cc7adb947d4927a7623134241805&aqi=no&q=" +
    String(document.getElementById("loc-input").value);
  // using link in a GET request, then turning it into json, then logging to console (need to remove that)
  data = fetch(fetchstr)
    .then((result) => result.json())
    .then((result) => console.log(result));

  // quick log test
  console.log("log2");
});

// quick log test
console.log("log3");

// stuff that puts the weather on the page (alternate object calling is becasue of errors)
document.getElementById("loc-name").innerHTML = data.location.name;
document.getElementById("loc-region").innerHTML = data.location.region;
document.getElementById("loc-country").innerHTML = data.location["country"];
document.getElementById("condition").innerHTML = data.current["condition.text"];
document.getElementById("condition-icon").innerHTML =
  data.current["condition.icon"];
