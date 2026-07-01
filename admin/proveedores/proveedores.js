(function () {

    const STORAGE_KEY = 'meier_proveedores';

    const $ = s => document.querySelector(s);

    const form = $('#proveedorForm');
    const table = $('#proveedoresTable');
    const total = $('#proveedoresTotal');

    let providers = [];

    function load() {
        try {
            providers = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            providers = [];
        }
    }

    function save() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(providers));
    }

    function render() {

        total.textContent = providers.length;

        if (providers.length === 0) {
            table.innerHTML = `
                <tr>
                    <td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">
                        No hay proveedores registrados.
                    </td>
                </tr>`;
            return;
        }

        table.innerHTML = providers.map((p, i) => `
            <tr>
                <td>${p.nombre}</td>
                <td>${p.telefono || '-'}</td>
                <td>${p.direccion || '-'}</td>
                <td>${p.contacto || '-'}</td>
                <td>
                    <button data-index="${i}" class="btn-delete">Eliminar</button>
                </td>
            </tr>
        `).join('');
    }

    form.addEventListener('submit', e => {
        e.preventDefault();

        const nombre = $('#nombre').value.trim();
        const telefono = $('#telefono').value.trim();
        const direccion = $('#direccion').value.trim();
        const contacto = $('#contacto').value.trim();
        const observaciones = $('#observaciones').value.trim();

        if (!nombre) return;

        providers.push({
            nombre,
            telefono,
            direccion,
            contacto,
            observaciones
        });

        save();
        render();
        form.reset();
    });

    table.addEventListener('click', e => {
        const btn = e.target.closest('[data-index]');
        if (!btn) return;

        providers.splice(Number(btn.dataset.index), 1);

        save();
        render();
    });

    load();
    render();

})();