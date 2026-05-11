const savedTheme = localStorage.getItem("theme") || "light";
document.documentElement.setAttribute("data-bs-theme", savedTheme);

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-bs-theme");
    const newTheme = currentTheme === "light" ? "dark" : "light";

    document.documentElement.setAttribute("data-bs-theme", newTheme);
    localStorage.setItem("theme", newTheme);

    const button = document.getElementById("themeToggleBtn");

    if (button) {
        button.innerText =
            newTheme === "light"
                ? "🌙 Dark Mode"
                : "☀️ Light Mode";
    }
}

window.onload = function () {
    const button = document.getElementById("themeToggleBtn");

    const currentTheme =
        document.documentElement.getAttribute("data-bs-theme");

    if (button) {
        button.innerText =
            currentTheme === "light"
                ? "🌙 Dark Mode"
                : "☀️ Light Mode";
    }
};