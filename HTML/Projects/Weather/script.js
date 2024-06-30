// magic stuff goes here (workin on it)
//quick log test
console.log("log1");
let data
// acquire data from api, then convert to json for actually usable stuff
document.getElementById("loc-submit").addEventListener('click', function(){
    // getting location to fetch data for, and combining it with api to create link
    let fetchstr = "https://api.weatherapi.com/v1/current.json?key=57cc7adb947d4927a7623134241805&aqi=no&q="+String(document.getElementById("loc-input").value);
    // using link in a GET request, then turning it into json, then logging to console (need to remove that)
    let data = fetch(fetchstr)
        .then(result => result.json())
        .then(result => console.log(result));

    // quick log test
    console.log("log2");
});

// quick log test
console.log("log3");

let ins_loc_name = data.location.name;
let ins_loc_region = data.location.region;
let ins_loc_country = data.location.country;
let ins_condition = data.current.condition.text;
let ins_condition_icon = data.current.condition.icon;

// jargon that actually puts the data on the page (i need to fix this)
document.getElementById("loc-name").innerHTML = data.location.name;
document.getElementById("loc-region").innerHTML = data.location.region;
document.getElementById("loc-country").innerHTML = data.location.country;
document.getElementById("condition").innerHTML = data.current.condition.text;
document.getElementById("condition-icon").innerHTML = data.current.condition.icon;
