document.addEventListener("DOMContentLoaded", () => {

    // Si ya hay sesión iniciada
    if (sessionStorage.getItem("admin") === "true") {
        window.location.replace("/admin/dashboard.html");
        return;
    }

    const form = document.getElementById("loginForm");
    const mensaje = document.getElementById("mensaje");
    const btnLogin = document.getElementById("btnLogin");

    if (!form) return;

    function mostrarMensaje(texto, tipo) {
        mensaje.textContent = texto;
        mensaje.className = `mensaje show ${tipo}`;
    }

    function limpiarMensaje() {
        mensaje.textContent = "";
        mensaje.className = "mensaje";
    }

    form.addEventListener("submit", async (e) => {

        e.preventDefault();

        limpiarMensaje();

        const usuario = document.getElementById("usuario").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!usuario || !password) {
            mostrarMensaje("Completa ambos campos para continuar.", "error");
            return;
        }

        btnLogin.disabled = true;
        btnLogin.textContent = "Ingresando...";

        let loginSuccess = false;

        try {
            if (window.supabaseClient) {
                const { data, error } = await window.supabaseClient.auth.signInWithPassword({
                    email: usuario,
                    password: password,
                });

                if (error) {
                    mostrarMensaje(error.message || "Usuario o contraseña incorrectos.", "error");
                } else if (data?.session?.user) {
                    const user = data.session.user;
                    sessionStorage.setItem("admin", "true");
                    sessionStorage.setItem("usuario", user.email || user.id || "admin");
                    mostrarMensaje("✔ Bienvenido, " + (user.email || "administrador") + ".", "success");
                    btnLogin.textContent = "¡Ingresando!";
                    loginSuccess = true;

                    setTimeout(() => {
                        window.location.href = "/admin/dashboard.html";
                    }, 900);
                } else {
                    mostrarMensaje("No se pudo iniciar sesión. Intenta de nuevo.", "error");
                }
            } else {
                if (
                    usuario.toLowerCase() === "daniel" &&
                    password === "Meierdan2026"
                ) {
                    sessionStorage.setItem("admin", "true");
                    sessionStorage.setItem("usuario", "Daniel");

                    mostrarMensaje("✔ Bienvenido, Daniel.", "success");
                    btnLogin.textContent = "¡Ingresando!";
                    loginSuccess = true;

                    setTimeout(() => {
                        window.location.href = "/admin/dashboard.html";
                    }, 900);
                } else {
                    mostrarMensaje("Usuario o contraseña incorrectos.", "error");
                }
            }
        } catch (error) {
            console.error(error);
            mostrarMensaje("Ocurrió un error inesperado. Intenta de nuevo.", "error");
        } finally {
            if (!loginSuccess) {
                btnLogin.disabled = false;
                btnLogin.textContent = "Ingresar";
            }
        }

    });

});