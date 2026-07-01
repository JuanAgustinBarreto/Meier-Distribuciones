(function () {

    const $ = id => document.getElementById(id);

    const parse = key => {
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
        }).format(value);

    const ventas = parse('meier_ventas');
    const compras = parse('meier_compras');
    const gastos = parse('meier_gastos');

    // =========================
    // TOTALES GENERALES
    // =========================

    const totalVentas = ventas.reduce((s, v) =>
        s + (Number(v.cantidad || 0) * Number(v.precio || 0)), 0);

    const totalCompras = compras.reduce((s, c) =>
        s + (Number(c.cantidad || 0) * Number(c.precio || 0)), 0);

    const totalGastos = gastos.reduce((s, g) =>
        s + Number(g.monto || 0), 0);

    const ganancia = totalVentas - totalCompras - totalGastos;

    $('totalVentas').textContent = format(totalVentas);
    $('totalCompras').textContent = format(totalCompras);
    $('totalGastos').textContent = format(totalGastos);
    $('ganancia').textContent = format(ganancia);

    // =========================
    // VENTAS ÚLTIMOS 7 DÍAS
    // =========================

    const hoy = new Date();
    const ultimos7 = [];

    for (let i = 6; i >= 0; i--) {
        const d = new Date();
        d.setDate(hoy.getDate() - i);

        const fechaStr = d.toISOString().split('T')[0];

        const totalDia = ventas
            .filter(v => v.fecha === fechaStr)
            .reduce((s, v) =>
                s + (Number(v.cantidad || 0) * Number(v.precio || 0)), 0);

        ultimos7.push({
            fecha: fechaStr,
            total: totalDia
        });
    }

    // =========================
    // GRAFICO SIMPLE (BARRAS)
    // =========================

    const chart = document.getElementById('chart');
    const max = Math.max(...ultimos7.map(d => d.total), 1);

    ultimos7.forEach(d => {

        const bar = document.createElement('div');
        bar.className = 'bar';

        const height = (d.total / max) * 200;

        bar.style.height = height + 'px';

        bar.innerHTML = `
            <span>${format(d.total)}</span>
            <small>${d.fecha.slice(5)}</small>
        `;

        chart.appendChild(bar);
    });

})();