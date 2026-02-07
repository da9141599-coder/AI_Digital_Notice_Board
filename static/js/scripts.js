// Auto-refresh for display board (every 10 seconds)
function autoRefreshBoard() {
    if (window.location.pathname.includes("/notice/display")) {
        setInterval(() => {
            location.reload();
        }, 10000);
    }
}
autoRefreshBoard();


// Fade-in animation for pages
document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll(".fade-in");
    elements.forEach(el => el.classList.add("fade-in"));
});


// Smooth scroll if needed
function smoothScrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}


// Example: Call AI prediction endpoint on typing notice text
async function predictCategory() {
    const inputBox = document.getElementById("id_content");
    const resultBox = document.getElementById("prediction_result");

    if (!inputBox || !resultBox) return;

    inputBox.addEventListener("keyup", async function () {
        const text = inputBox.value;

        if (text.length < 10) {
            resultBox.innerHTML = "";
            return;
        }

        const response = await fetch("/api/predict/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();
        resultBox.innerHTML = `<span class="badge bg-success">${data.prediction}</span>`;
    });
}
predictCategory();
