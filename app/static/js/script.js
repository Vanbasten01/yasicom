
 function toggleMenu() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }

function toggleMenu() {
  var x = document.getElementById("myTopnav");
  x.classList.toggle("responsive");
}


 function redirectToDashboard() {
        window.location.href = "{{ url_for('routes.dashboard') }}";
    }
