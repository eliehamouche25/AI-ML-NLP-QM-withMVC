 document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll("#menu > ul > li > a");

  menuItems.forEach((item) => {
    item.addEventListener("click", function (e) {
      e.preventDefault();

      const submenu = this.nextElementSibling;

      // Close all submenus
      document.querySelectorAll(".submenu").forEach((sub) => {
        if (sub !== submenu) sub.style.display = "none";
      });

      // Toggle the clicked one
      if (submenu && submenu.classList.contains("submenu")) {
        submenu.style.display = submenu.style.display === "block" ? "none" : "block";
      }
    });
  });
});


document.addEventListener("DOMContentLoaded", () => {
  const logo = document.querySelector(".logo");
  if (logo) {
    // trigger animation by adding class after short delay
    setTimeout(() => {
      logo.classList.add("animate");
    }, 100);
  }
});