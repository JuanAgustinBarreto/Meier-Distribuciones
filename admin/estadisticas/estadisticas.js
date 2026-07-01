(function () {

    const getJSON = key => {
        try {
            return JSON.parse(localStorage.getItem(key) || '[]');
        } catch {
            return [];
        }
    };

    const format = value =>
        new Intl.NumberFormat('es-AR', {
            style: 'currency',
            currency: 'ARS'
        }).format(value || 0);

    const ventas = getJSON('meier_ventas');
    const compras = getJSON('meier_compras');
    const gastos = getJSON('meier_gastos');
    const clientes = getJSON('meier_clientes');

    const totalVentas = ventas.reduce((sum, v) => {
        const cantidad = Number(v.cantidad || 0);
        const precio = Number(v.precio || 0);
        return sum + (cantidad * precio);
    }, 0);

    const totalCompras = compras.reduce((sum, c) => {
        const cantidad = Number(c.cantidad || 0);
        const precio = Number(c.precio || 0);
        return sum + (cantidad * precio);
    }, 0);

    const totalGastos = gastos.reduce((sum, g) => {
        return sum + Number(g.monto || 0);
    }, 0);

    // UI
    document.getElementById('statVentas').textContent = format(totalVentas);
    document.getElementById('statCompras').textContent = format(totalCompras);
    document.getElementById('statGastos').textContent = format(totalGastos);
    document.getElementById('statClientes').textContent = clientes.length;

    document.getElementById('monthSummary').textContent =
        `Ingresos: ${format(totalVentas)} | Compras: ${format(totalCompras)} | Gastos: ${format(totalGastos)} | Clientes: ${clientes.length}`;

})();