(function(){
    const STORAGE_KEY = 'meier_compras';
    const $ = selector => document.querySelector(selector);
    const form = $('#compraForm');
    const table = $('#comprasTable');
    const total = $('#comprasTotal');
    const valor = $('#comprasValor');
    let compras = [];

    function load(){
        try {
            compras = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            compras = [];
        }
    }

    function save(){
        localStorage.setItem(STORAGE_KEY, JSON.stringify(compras));
    }

    function render(){
        total.textContent = compras.length;
        const totalValor = compras.reduce((sum, compra) => sum + Number(compra.cantidad) * Number(compra.precio), 0);
        valor.textContent = new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(totalValor);
        if(!compras.length){
            table.innerHTML = '<tr><td colspan="6" style="padding:18px;text-align:center;color:#6b7280;">No hay compras registradas.</td></tr>';
            return;
        }
        table.innerHTML = compras.map((compra,index) => `
            <tr>
                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.producto}</td>
                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.proveedor}</td>
                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.cantidad}</td>
                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${new Intl.NumberFormat('es-AR',{style:'currency',currency:'ARS'}).format(compra.precio)}</td>
                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.fecha}</td>
                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>
            </tr>`).join('');
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        const producto = $('#producto').value.trim();
        const proveedor = $('#proveedor').value.trim();
        const cantidad = Number($('#cantidad').value) || 0;
        const precio = Number($('#precio').value) || 0;
        const fecha = $('#fecha').value;
        const notas = $('#notas').value.trim();
        if(!producto || !proveedor || !fecha) return;
        compras.push({ producto, proveedor, cantidad, precio, fecha, notas });
        save();
        render();
        form.reset();
    });

    table.addEventListener('click', event => {
        const button = event.target.closest('[data-index]');
        if(!button) return;
        compras.splice(Number(button.dataset.index), 1);
        save();
        render();
    });

    load();
    render();
})();