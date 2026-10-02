function showWelcome() {
    alert("Welcome to my portfolio!");
}
const form = document.getElementById("contactForm");
const formMessage = document.getElementById("formMessage");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    formMessage.textContent = "Thank you! Your message has been submitted.";

    form.reset();
});