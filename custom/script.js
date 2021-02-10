function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function toggle() {
  button = document.getElementById("toggle");
  if (button.className === "fas fa-sun") {
    button.className = "fas fa-moon";
    document.body.style.backgroundColor = "#222";
    document.body.style.color = "#f7f7f7";
  } else {
    button.className = "fas fa-sun";
    document.body.style.backgroundColor = "#f7f7f7";
    document.body.style.color = "#222";
  }

}
