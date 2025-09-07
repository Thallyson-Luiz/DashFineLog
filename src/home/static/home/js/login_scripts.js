document.getElementById("loginpage").classList.add("active");

// Função para alternar a visibilidade da senha
function togglePassword() {
    const passwordField = document.getElementById("passwordField");
    const toggleIcon = document.getElementById("toggleIcon");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleIcon.className = "fas fa-eye-slash";
    } else {
        passwordField.type = "password";
        toggleIcon.className = "fas fa-eye";
    }
}

// Aguarda o DOM estar completamente carregado
document.addEventListener("DOMContentLoaded", function () {
    // Seleção de elementos
    const loginForm = document.querySelector("form");
    const textInput = document.querySelector('input[name="username"]');
    const passwordInput = document.querySelector("#passwordField");
    const submitButton = document.querySelector('button[type="submit"]');
    const tryLaterLink = document.querySelector(".try-later");

    // Função para validar username
    function isValidUsername(username) {
        if (username.length < 4) {
            return false;
        }
        return true;
    }

    // Função para mostrar mensagem de erro
    function showError(message) {
        // Remove erro anterior se existir
        const existingAlert = document.querySelector(".alert-danger");
        if (existingAlert) {
            existingAlert.remove();
        }

        // Cria nova mensagem de erro
        const alertDiv = document.createElement("div");
        alertDiv.className = "alert alert-danger";
        alertDiv.setAttribute("role", "alert");
        alertDiv.textContent = message;

        // Insere antes do primeiro campo do formulário
        const firstFormGroup = document.querySelector(".mb-3");
        firstFormGroup.parentNode.insertBefore(alertDiv, firstFormGroup);

        // Remove a mensagem após 5 segundos
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }

    // Função para mostrar mensagem de sucesso
    function showSuccess(message) {
        const alertDiv = document.createElement("div");
        alertDiv.className = "alert alert-success";
        alertDiv.setAttribute("role", "alert");
        alertDiv.textContent = message;

        const firstFormGroup = document.querySelector(".mb-3");
        firstFormGroup.parentNode.insertBefore(alertDiv, firstFormGroup);

        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 3000);
    }

    // Função para adicionar classe de erro ao campo
    function addFieldError(field) {
        field.classList.add("is-invalid");
        field.parentElement.style.borderColor = "#dc3545";
    }

    // Função para remover classe de erro do campo
    function removeFieldError(field) {
        field.classList.remove("is-invalid");
        field.parentElement.style.borderColor = "";
    }

    // Validação em tempo real para o campo de username
    textInput.addEventListener("input", function () {
        removeFieldError(this);
        if (this.value && !isValidUsername(this.value)) {
            addFieldError(this);
        }
    });

    // Validação em tempo real para o campo de senha
    passwordInput.addEventListener("input", function () {
        removeFieldError(this);
        if (this.value && this.value.length < 6) {
            addFieldError(this);
        }
    });

    // Função para desabilitar/habilitar botão de submit
    function toggleSubmitButton(disabled) {
        submitButton.disabled = disabled;
        if (disabled) {
            submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Entrando...';
            submitButton.classList.add("loading");
        } else {
            submitButton.innerHTML = "Sign In";
            submitButton.classList.remove("loading");
        }
    }

    // Manipulador do envio do formulário
    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const username = textInput.value.trim();
        const password = passwordInput.value;

        // Remove erros anteriores
        removeFieldError(textInput);
        removeFieldError(passwordInput);

        // Validações
        let hasError = false;

        if (!username) {
            showError("O campo usuário é obrigatório.");
            addFieldError(textInput);
            hasError = true;
        } else if (!isValidUsername(username)) {
            showError("Por favor, insira um usuário válido.");
            addFieldError(textInput);
            hasError = true;
        }

        if (!password) {
            showError("O campo senha é obrigatório.");
            addFieldError(passwordInput);
            hasError = true;
        } else if (password.length < 4) {
            showError("A senha deve ter pelo menos 4 caracteres.");
            addFieldError(passwordInput);
            hasError = true;
        }

        if (hasError) {
            return;
        }

        // Simular envio do formulário
        toggleSubmitButton(true);

        // Envia o formulario
        loginForm.submit();
    });

    // Adicionar efeitos visuais aos campos de input
    const inputFields = [textInput, passwordInput];

    inputFields.forEach((field) => {
        field.addEventListener("focus", function () {
            this.parentElement.classList.add("focused");
        });

        field.addEventListener("blur", function () {
            if (!this.value) {
                this.parentElement.classList.remove("focused");
            }
        });
    });

    // Adicionar animações de entrada
    function addEntranceAnimations() {
        const elements = [".logo", ".welcome-title", ".welcome-subtitle", ".mb-3", ".btn-primary"];

        elements.forEach((selector, index) => {
            const element = document.querySelector(selector);
            if (element) {
                element.style.opacity = "0";
                element.style.transform = "translateY(20px)";
                element.style.transition = "opacity 0.6s ease, transform 0.6s ease";

                setTimeout(() => {
                    element.style.opacity = "1";
                    element.style.transform = "translateY(0)";
                }, index * 150);
            }
        });
    }

    // Ativar animações de entrada
    addEntranceAnimations();

    // Detectar tecla Enter nos campos de input
    inputFields.forEach((field) => {
        field.addEventListener("keypress", function (e) {
            if (e.key === "Enter") {
                loginForm.dispatchEvent(new Event("submit"));
            }
        });
    });

    // Função para salvar dados do formulário no localStorage (opcional)
    function saveFormData() {
        const formData = {
            username: textInput.value,
            rememberMe: true, // Adicione checkbox se necessário
        };

        if (textInput.value) {
            localStorage.setItem("loginFormData", JSON.stringify(formData));
        }
    }

    // Função para carregar dados salvos
    function loadFormData() {
        const savedData = localStorage.getItem("loginFormData");
        if (savedData) {
            const data = JSON.parse(savedData);
            textInput.value = data.username || "";

            // Adicionar classe focused se houver valor
            if (textInput.value) {
                textInput.parentElement.classList.add("focused");
            }
        }
    }

    // Carregar dados salvos ao iniciar
    loadFormData();

    // Salvar dados quando o usuário digitar no campo username
    textInput.addEventListener("input", saveFormData);

    // Limpar dados salvos ao fazer logout
    window.clearSavedLoginData = function () {
        localStorage.removeItem("loginFormData");
    };

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
});
