var typed = new Typed("#typed", {
  strings: ["Programmer", "Web Developer", "Student", "Graphic Designer"],
  typeSpeed: 60,
  backSpeed: 60,
  loop: true,
});

$(document).ready(function () {
  // Transition effect for navbar
  $(window).scroll(function () {
    // checks if window is scrolled more than 500px, adds/removes solid class
    if ($(this).scrollTop() > 20) {
      $(".nav").addClass("solid-navbar-bg h1", 300);
    } else {
      $(".nav").removeClass("solid-navbar-bg h1", 300);
    }
  });
});
