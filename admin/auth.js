// ============================================
// Meier Distribuciones ERP
// auth.js
// Control de sesión del administrador
// ============================================

(function () {

    "use strict";

    const LOGIN_PAGE = "/admin/login.html";
    const DASHBOARD_PAGE = "/admin/dashboard.html";

    /**
     * Verifica si existe una sesión activa
     */
    async function sesionActiva() {

        if (sessionStorage.getItem("admin") === "true") {
            return true;
        }

        if (window.supabaseClient) {
            try {
                const { data } = await window.supabaseClient.auth.getSession();
                const session = data?.session;

                if (session?.user) {
                    sessionStorage.setItem("admin", "true");
                    sessionStorage.setItem("usuario", session.user.email || session.user.id || "admin");
                    return true;
                }
            } catch (error) {
                console.error("Error verificando sesión Supabase:", error);
            }
        }

        return false;

    }

    /**
     * Obtiene el usuario logueado
     */
    function obtenerUsuario() {

        return sessionStorage.getItem("usuario") || "";

    }

    /**
     * Cierra la sesión
     */
    async function cerrarSesion() {

        sessionStorage.clear();

        if (window.supabaseClient) {
            try {
                await window.supabaseClient.auth.signOut();
            } catch (error) {
                console.warn("No se pudo cerrar sesión en Supabase:", error);
            }
        }

        window.location.replace(LOGIN_PAGE);

    }

    /**
     * Protege cualquier página del panel
     */
    async function protegerPagina() {

        const ruta = window.location.pathname.toLowerCase();

        // No proteger el login
        if (ruta.endsWith("/login.html")) {
            return;
        }

        if (!(await sesionActiva())) {
            window.location.replace(LOGIN_PAGE);
        }

    }

    /**
     * Evita volver al login si ya inició sesión
     */
    async function verificarLogin() {

        const ruta = window.location.pathname.toLowerCase();

        if (!ruta.endsWith("/login.html")) {
            return;
        }

        if (await sesionActiva()) {
            window.location.replace(DASHBOARD_PAGE);
        }

    }

    /**
     * Expone funciones globales
     */
    window.Auth = {

        sesionActiva,

        obtenerUsuario,

        cerrarSesion

    };

    protegerPagina();

    verificarLogin();

})();