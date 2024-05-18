document.addEventListener("click", function (event) {
  // Checking if the button was clicked
  if (!event.target.matches("#submit")) return;

    let locinput = document.getElementById("loc-input").value;
  fetch("<https://api.weatherapi.com/v1/current.json?key=da3f180c41a84bdcb30230004242104&q=98354&aqi=yes>")
    .then((response) => response.json())
    .then((data) => console.log(data));
});