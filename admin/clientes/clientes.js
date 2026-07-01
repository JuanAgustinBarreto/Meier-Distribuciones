(function () {
    const STORAGE_KEY = 'meier_clientes';

    const $ = s => document.querySelector(s);

    const form = $('#clienteForm');
    const table = $('#clientesTable');
    const total = $('#clientesTotal');

    let clientes = [];

    function load() {
        try {
            clientes = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            clientes = [];
        }
    }

    function save() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(clientes));
    }

    function render() {
        total.textContent = clientes.length;

        if (clientes.length === 0) {
            table.innerHTML = `
                <tr>
                    <td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">
                        No hay clientes registrados.
                    </td>
                </tr>`;
            return;
        }

        table.innerHTML = clientes.map((c, i) => `
            <tr>
                <td>${c.nombre}</td>
                <td>${c.email || '-'}</td>
                <td>${c.telefono || '-'}</td>
                <td>${c.direccion || '-'}</td>
                <td>
                    <button data-index="${i}" class="btn-delete">Eliminar</button>
                </td>
            </tr>
        `).join('');
    }

    form.addEventListener('submit', e => {
        e.preventDefault();

        const nombre = $('#nombre').value.trim();
        const email = $('#email').value.trim();
        const telefono = $('#telefono').value.trim();
        const direccion = $('#direccion').value.trim();

        if (!nombre) return;

        // 🔥 evitar duplicados por email
        const exists = clientes.some(c => c.email && email && c.email === email);
        if (exists) {
            alert('Ya existe un cliente con ese email');
            return;
        }

        clientes.push({ nombre, email, telefono, direccion });

        save();
        render();
        form.reset();
    });

    table.addEventListener('click', e => {
        const btn = e.target.closest('[data-index]');
        if (!btn) return;

        clientes.splice(Number(btn.dataset.index), 1);

        save();
        render();
    });

    load();
    render();
})();