// =====================================================
// Meier Distribuciones ERP
// Conexión oficial con Supabase
// =====================================================

"use strict";

/*
|--------------------------------------------------------------------------
| CONFIGURACIÓN
|--------------------------------------------------------------------------
*/

const SUPABASE_URL =
    "https://rtvbxgwrafqgqvqohqyq.supabase.co";

const SUPABASE_KEY =
    "sb_publishable__KGWA7hw65KiiGbMVy-sb_publishable__KGWA7hw65KiiGbMVy-UdQ_Sc1937Gf";

/*
|--------------------------------------------------------------------------
| CLIENTE SUPABASE
|--------------------------------------------------------------------------
*/

const supabase = window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_KEY,
    {
        auth: {

            persistSession: true,

            autoRefreshToken: true,

            detectSessionInUrl: false

        }
    }
);

/*
|--------------------------------------------------------------------------
| EXPORTAR GLOBALMENTE
|--------------------------------------------------------------------------
*/

window.supabaseClient = supabase;

/*
|--------------------------------------------------------------------------
| VERIFICAR CONEXIÓN
|--------------------------------------------------------------------------
*/

async function verificarConexion() {

    try {

        const { error } = await supabase
            .from("productos")
            .select("id")
            .limit(1);

        if (error) {

            console.error("Supabase:", error.message);

            return false;

        }

        console.log("✅ Supabase conectado correctamente");

        return true;

    }

    catch (err) {

        console.error("Error de conexión:", err);

        return false;

    }

}

window.verificarConexion = verificarConexion;