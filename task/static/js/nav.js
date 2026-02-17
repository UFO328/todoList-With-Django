const burger = document.querySelector(".navbar-burger");
const menu = document.getElementById("navbarMenu");

  burger.addEventListener("click", () => {
    burger.classList.toggle("is-active");
    menu.classList.toggle("is-active");
  });