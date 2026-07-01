document.addEventListener("DOMContentLoaded", () => {

    const $ = (id) => document.getElementById(id);

    const get = (key) => JSON.parse(localStorage.getItem(key) || "[]");

    const format = (n) =>
        new Intl.NumberFormat("es-AR", { style: "currency", currency: "ARS" }).format(n || 0);

    // ======================
    // DATA
    // ======================

    const ventas = get("meier_ventas");
    const productos = get("meier_productos");
    const clientes = get("meier_clientes");
    const stock = get("meier_stock");

    // ======================
    // FECHA
    // ======================

    $("fechaActual").textContent = new Date().toLocaleDateString("es-AR");

    // ======================
    // KPI
    // ======================

    const ventasHoy = ventas.filter(v =>
        v.fecha === new Date().toISOString().slice(0,10)
    ).reduce((a,b)=>a+(b.cantidad*b.precio),0);

    const ventasMes = ventas.reduce((a,b)=>a+(b.cantidad*b.precio),0);

    const stockBajo = stock.filter(s => s.cantidad < 5).length;

    $("ventasHoy").textContent = format(ventasHoy);
    $("ventasMes").textContent = format(ventasMes);
    $("productos").textContent = productos.length;
    $("clientes").textContent = clientes.length;
    $("stockBajo").textContent = stockBajo;

    // ======================
    // TOP PRODUCTOS
    // ======================

    const top = {};

    ventas.forEach(v => {
        top[v.producto] = (top[v.producto] || 0) + v.cantidad;
    });

    const topArray = Object.entries(top)
        .sort((a,b)=>b[1]-a[1])
        .slice(0,5);

    $("topProductos").innerHTML = topArray
        .map(p => `<li>${p[0]} - <b>${p[1]}</b></li>`)
        .join("");

    // ======================
    // ÚLTIMAS VENTAS
    // ======================

    $("ultimasVentas").innerHTML = ventas.slice(-5).reverse().map(v => `
        <div style="padding:10px;border-bottom:1px solid #eee">
            ${v.producto} | ${v.cantidad} | ${format(v.precio * v.cantidad)}
        </div>
    `).join("");

    // ======================
    // CHART
    // ======================

    const dias = {};
    ventas.forEach(v => {
        dias[v.fecha] = (dias[v.fecha] || 0) + (v.cantidad * v.precio);
    });

    const labels = Object.keys(dias).slice(-7);
    const data = Object.values(dias).slice(-7);

    new Chart(document.getElementById("chartVentas"), {
        type: "line",
        data: {
            labels,
            datasets: [{
                label: "Ventas",
                data,
                borderWidth: 2
            }]
        }
    });

});