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

let client;
const client_id_google = "1011975736026-t18s4p91b8hbl12t78mu445nlblbqevi.apps.googleusercontent.com";

window.onload = function () {
    client = google.accounts.oauth2.initTokenClient({
        client_id: client_id_google,
        scope: "email profile openid",
        callback: (response) => {
            console.log("Token do Google:", response.access_token);

            fetch("http://127.0.0.1:8000/perfil/google/callback", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ token: response.access_token }),
            })
                .then((res) => {
                    if (!res.ok) {
                        // Lança erro para cair no catch
                        return res.json().then((err) => {
                            throw new Error(err.detail || "Erro no backend");
                        });
                    }
                    return res.json();
                })
                .then((data) => {
                    console.log("Usuário autenticado:", data);
                    alert("Usuário autenticado com sucesso!");
                })
                .catch((error) => {
                    console.error("Falha na autenticação:", error.message);
                    alert("Erro ao autenticar com Google. Tente novamente.");
                });
        },
    });

    document.getElementById("google-login").addEventListener("click", () => {
        client.requestAccessToken();
        alert("Atenção: O processo de autenticação ainda está em analise pelo google, por favor, use a autenticação normal do site.");
    });
};
