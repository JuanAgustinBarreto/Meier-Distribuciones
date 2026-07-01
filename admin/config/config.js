(function () {

    const STORAGE_KEY = 'meier_config';

    const $ = s => document.querySelector(s);

    const form = $('#configForm');

    const storeName = $('#storeName');
    const currency = $('#currency');
    const taxRate = $('#taxRate');
    const storeNotes = $('#storeNotes');

    function load() {
        try {
            const cfg = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');

            storeName.value = cfg.storeName || '';
            currency.value = cfg.currency || 'ARS';
            taxRate.value = cfg.taxRate ?? 0;
            storeNotes.value = cfg.storeNotes || '';

        } catch {
            // fallback silencioso
        }
    }

    function saveConfig(data) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    }

    form.addEventListener('submit', e => {
        e.preventDefault();

        const config = {
            storeName: storeName.value.trim(),
            currency: currency.value,
            taxRate: Number(taxRate.value) || 0,
            storeNotes: storeNotes.value.trim()
        };

        saveConfig(config);

        // feedback simple (después lo mejoramos a toast)
        alert('Configuración guardada correctamente');
    });

    load();

})();