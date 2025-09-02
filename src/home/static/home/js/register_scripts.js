document.getElementById("registerpage").classList.add("active");

function togglePassword(fieldId, iconId) {
    const passwordField = document.getElementById(fieldId);
    const toggleIcon = document.getElementById(iconId);

    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleIcon.classList.remove("fa-eye");
        toggleIcon.classList.add("fa-eye-slash");
    } else {
        passwordField.type = "password";
        toggleIcon.classList.remove("fa-eye-slash");
        toggleIcon.classList.add("fa-eye");
    }
}

// Validação de senhas em tempo real
document.addEventListener("DOMContentLoaded", function () {
    const passwordField = document.getElementById("passwordField");
    const confirmPasswordField = document.getElementById("confirmPasswordField");
    const form = document.querySelector("form");

    function validatePasswords() {
        if (confirmPasswordField.value !== "" && passwordField.value !== confirmPasswordField.value) {
            confirmPasswordField.setCustomValidity("As senhas não coincidem");
            confirmPasswordField.style.borderColor = "#dc3545";
        } else {
            confirmPasswordField.setCustomValidity("");
            if (confirmPasswordField.value !== "") {
                confirmPasswordField.style.borderColor = "#28a745";
            }
        }
    }

    passwordField.addEventListener("input", validatePasswords);
    confirmPasswordField.addEventListener("input", validatePasswords);

    form.addEventListener("submit", function (e) {
        if (passwordField.value !== confirmPasswordField.value) {
            e.preventDefault();
            alert("As senhas não coincidem!");
            return false;
        }

        if (passwordField.value.length < 6) {
            e.preventDefault();
            alert("A senha deve ter pelo menos 6 caracteres!");
            return false;
        }
    });
});
