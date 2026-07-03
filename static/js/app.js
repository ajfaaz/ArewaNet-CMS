document.addEventListener("DOMContentLoaded", function () {
    console.log("ArewaNet NGO CMS Loaded");

    // Navbar Scroll Shadow Effect
    const nav = document.querySelector(".navbar");

    if (nav) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 60) {
                nav.classList.add("shadow");
            } else {
                nav.classList.remove("shadow");
            }
        });
    }
});