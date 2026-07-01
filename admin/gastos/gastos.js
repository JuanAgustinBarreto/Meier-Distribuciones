(function () {

    const STORAGE_KEY = 'meier_gastos';

    const $ = s => document.querySelector(s);

    const form = $('#gastosForm');
    const tabla = $('#tablaGastos');
    const total = $('#totalGastos');

    let gastos = [];

    function load() {
        try {
            gastos = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            gastos = [];
        }
    }

    function save() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(gastos));
    }

    function format(value) {
        return new Intl.NumberFormat('es-AR', {
            style: 'currency',
            currency: 'ARS'
        }).format(value || 0);
    }

    function calcularTotal() {
        return gastos.reduce((sum, g) => {
            return sum + Number(g.monto || 0);
        }, 0);
    }

    function render() {

        total.textContent = format(calcularTotal());

        if (gastos.length === 0) {
            tabla.innerHTML = `
                <tr>
                    <td colspan="6" style="padding:18px;text-align:center;color:#6b7280;">
                        No hay gastos registrados.
                    </td>
                </tr>`;
            return;
        }

        tabla.innerHTML = gastos.map((g, i) => `
            <tr>
                <td>${g.concepto}</td>
                <td>${format(g.monto)}</td>
                <td>${g.fecha || '-'}</td>
                <td>${g.categoria}</td>
                <td>${g.notas || ''}</td>
                <td>
                    <button data-index="${i}" class="btn-delete">Eliminar</button>
                </td>
            </tr>
        `).join('');
    }

    form.addEventListener('submit', e => {
        e.preventDefault();

        const data = Object.fromEntries(new FormData(form).entries());

        const gasto = {
            concepto: data.concepto.trim(),
            monto: Number(data.monto),
            fecha: data.fecha,
            categoria: data.categoria,
            notas: (data.notas || '').trim()
        };

        if (!gasto.concepto || gasto.monto <= 0 || !gasto.fecha) return;

        gastos.push(gasto);

        save();
        render();
        form.reset();
    });

    tabla.addEventListener('click', e => {
        const btn = e.target.closest('[data-index]');
        if (!btn) return;

        gastos.splice(Number(btn.dataset.index), 1);

        save();
        render();
    });

    load();
    render();

})();