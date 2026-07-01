(function () {

    const VENTAS_KEY = 'meier_ventas';
    const PRODUCTOS_KEY = 'meier_productos';

    const $ = s => document.querySelector(s);

    const form = $('#ventasForm');
    const table = $('#ventasTable');
    const totalEl = $('#ventasTotal');
    const ingresosEl = $('#ventasIngresos');
    const productoSelect = $('#producto');

    let ventas = [];
    let productos = [];

    function load() {
        ventas = JSON.parse(localStorage.getItem(VENTAS_KEY) || '[]');
        productos = JSON.parse(localStorage.getItem(PRODUCTOS_KEY) || '[]');
    }

    function save() {
        localStorage.setItem(VENTAS_KEY, JSON.stringify(ventas));
        localStorage.setItem(PRODUCTOS_KEY, JSON.stringify(productos));
    }

    function format(value) {
        return new Intl.NumberFormat('es-AR', {
            style: 'currency',
            currency: 'ARS'
        }).format(value || 0);
    }

    function loadProductsSelect() {
        productoSelect.innerHTML = `
            <option value="">Seleccionar producto</option>
        ` + productos.map(p => `
            <option value="${p.nombre}">${p.nombre} (Stock: ${p.stock})</option>
        `).join('');
    }

    function updateStock(productName, quantity) {
        const product = productos.find(p => p.nombre === productName);
        if (!product) return false;

        if (product.stock < quantity) return false;

        product.stock -= quantity;
        return true;
    }

    function render() {

        totalEl.textContent = ventas.length;

        const ingresos = ventas.reduce((s, v) => s + v.cantidad * v.precio, 0);
        ingresosEl.textContent = format(ingresos);

        if (ventas.length === 0) {
            table.innerHTML = `<tr><td colspan="5">No hay ventas</td></tr>`;
            return;
        }

        table.innerHTML = ventas.map((v, i) => `
            <tr>
                <td>${v.producto}</td>
                <td>${v.cantidad}</td>
                <td>${format(v.precio)}</td>
                <td>${v.fecha}</td>
                <td><button data-index="${i}">Eliminar</button></td>
            </tr>
        `).join('');
    }

    form.addEventListener('submit', e => {
        e.preventDefault();

        const producto = $('#producto').value;
        const cantidad = Number($('#cantidad').value);
        const precio = Number($('#precio').value);
        const fecha = $('#fecha').value;
        const notas = $('#notas').value;

        if (!producto || !fecha) return;

        // 🚨 VALIDAR STOCK
        if (!updateStock(producto, cantidad)) {
            alert('Stock insuficiente');
            return;
        }

        ventas.push({ producto, cantidad, precio, fecha, notas });

        save();
        render();
        loadProductsSelect();
        form.reset();
    });

    table.addEventListener('click', e => {
        const btn = e.target.closest('[data-index]');
        if (!btn) return;

        ventas.splice(Number(btn.dataset.index), 1);

        save();
        render();
    });

    load();
    loadProductsSelect();
    render();

})();