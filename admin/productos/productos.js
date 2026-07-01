(function () {

    const STORAGE_KEY = 'meier_productos';

    const $ = s => document.querySelector(s);

    const form = $('#productoForm');
    const table = $('#productosTable');
    const count = $('#productosCount');
    const stockTotalEl = $('#stockTotal');

    let products = [];

    function load() {
        try {
            products = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            products = [];
        }
    }

    function save() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(products));
    }

    function format(value) {
        return new Intl.NumberFormat('es-AR', {
            style: 'currency',
            currency: 'ARS'
        }).format(value || 0);
    }

    function totalStock() {
        return products.reduce((sum, p) => sum + Number(p.stock || 0), 0);
    }

    function render() {

        count.textContent = products.length;
        stockTotalEl.textContent = totalStock();

        if (products.length === 0) {
            table.innerHTML = `
                <tr>
                    <td colspan="6" style="padding:18px;text-align:center;color:#6b7280;">
                        No hay productos registrados.
                    </td>
                </tr>`;
            return;
        }

        table.innerHTML = products.map((p, i) => `
            <tr>
                <td>${p.nombre}</td>
                <td>${p.marca || '-'}</td>
                <td>${p.categoria || '-'}</td>
                <td>${format(p.precio)}</td>
                <td>${p.stock}</td>
                <td>
                    <button data-index="${i}" class="btn-delete">Eliminar</button>
                </td>
            </tr>
        `).join('');
    }

    form.addEventListener('submit', e => {
        e.preventDefault();

        const nombre = $('#prodNombre').value.trim();
        const marca = $('#prodMarca').value.trim();
        const categoria = $('#prodCategoria').value.trim();
        const precio = Number($('#prodPrecio').value);
        const stock = Number($('#prodStock').value);
        const descripcion = $('#prodDescripcion').value.trim();

        if (!nombre || precio < 0 || stock < 0) return;

        products.push({
            nombre,
            marca,
            categoria,
            precio,
            stock,
            descripcion
        });

        save();
        render();
        form.reset();
    });

    table.addEventListener('click', e => {
        const btn = e.target.closest('[data-index]');
        if (!btn) return;

        products.splice(Number(btn.dataset.index), 1);

        save();
        render();
    });

    load();
    render();

})();