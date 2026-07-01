(function () {

    const PRODUCTS_KEY = 'meier_productos';

    const $ = s => document.querySelector(s);

    const table = $('#stockTable');
    const totalProductos = $('#totalProductos');
    const totalStock = $('#totalStock');

    function getProducts() {
        try {
            return JSON.parse(localStorage.getItem(PRODUCTS_KEY) || '[]');
        } catch {
            return [];
        }
    }

    function format(value) {
        return new Intl.NumberFormat('es-AR', {
            style: 'currency',
            currency: 'ARS'
        }).format(value || 0);
    }

    function render() {

        const products = getProducts();

        totalProductos.textContent = products.length;

        const stockTotal = products.reduce((s, p) => s + Number(p.stock || 0), 0);
        totalStock.textContent = stockTotal;

        if (products.length === 0) {
            table.innerHTML = `
                <tr>
                    <td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">
                        No hay productos cargados.
                    </td>
                </tr>`;
            return;
        }

        table.innerHTML = products.map(p => `
            <tr>
                <td>${p.nombre}</td>
                <td>${p.marca || '-'}</td>
                <td>${p.categoria || '-'}</td>
                <td>${p.stock}</td>
                <td>${format(p.stock * p.precio)}</td>
            </tr>
        `).join('');
    }

    render();

})();