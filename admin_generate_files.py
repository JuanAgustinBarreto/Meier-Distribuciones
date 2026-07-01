from pathlib import Path

base = Path('admin')

FILES = {
    'clientes/clientes.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clientes | Meier Distribuciones</title>
    <link rel="stylesheet" href="../admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="../auth.js"></script>

<div class="dashboard">

    <aside class="sidebar">

        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="../dashboard.html">🏠 Dashboard</a>
            <a href="../productos/productos.html">📦 Productos</a>
            <a href="../ventas/ventas.html">🛒 Ventas</a>
            <a href="../compras.html">🚚 Compras</a>
            <a href="../proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="clientes.html">👥 Clientes</a>
            <a href="../gastos/gastos.html">💰 Gastos</a>
            <a href="../reportes.html">📈 Reportes</a>
            <a href="../estadisticas/estadisticas.html">📊 Estadísticas</a>
            <a href="../stock/index.html">📦 Stock</a>
            <a href="../config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>

    </aside>

    <main>

        <h1>Clientes</h1>

        <div class="cards">
            <div class="card">
                <h3>Total clientes</h3>
                <h2 id="clientesTotal">0</h2>
            </div>
        </div>

        <section style="background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);margin-top:20px;">
            <h2>Registrar cliente</h2>
            <form id="clienteForm" style="display:grid;gap:14px;margin-top:18px;">
                <input type="text" id="nombre" placeholder="Nombre" required>
                <input type="email" id="email" placeholder="Correo electrónico">
                <input type="text" id="telefono" placeholder="Teléfono">
                <textarea id="direccion" rows="3" placeholder="Dirección"></textarea>
                <button type="submit">Guardar cliente</button>
            </form>
        </section>

        <section style="margin-top:30px;background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);">
            <h2>Lista de clientes</h2>
            <div style="overflow-x:auto;margin-top:18px;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f6f7fb;">
                            <th style="padding:12px;text-align:left;">Nombre</th>
                            <th style="padding:12px;text-align:left;">Email</th>
                            <th style="padding:12px;text-align:left;">Teléfono</th>
                            <th style="padding:12px;text-align:left;">Dirección</th>
                            <th style="padding:12px;text-align:left;">Acción</th>
                        </tr>
                    </thead>
                    <tbody id="clientesTable">
                        <tr>
                            <td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">No hay clientes registrados.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

    </main>

</div>

<script src="clientes.js"></script>

</body>

</html>''',
    'clientes/clientes.js': '''(function(){
    const STORAGE_KEY = 'meier_clientes';
    const $ = selector => document.querySelector(selector);
    const form = $('#clienteForm');
    const table = $('#clientesTable');
    const total = $('#clientesTotal');
    let clientes = [];

    function load(){
        try {
            clientes = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            clientes = [];
        }
    }

    function save(){
        localStorage.setItem(STORAGE_KEY, JSON.stringify(clientes));
    }

    function render(){
        total.textContent = clientes.length;
        if(!clientes.length){
            table.innerHTML = '<tr><td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">No hay clientes registrados.</td></tr>';
            return;
        }
        table.innerHTML = clientes.map((cliente,index) => `\n            <tr>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${cliente.nombre}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${cliente.email||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${cliente.telefono||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${cliente.direccion||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>\n            </tr>`).join('');
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        const nombre = $('#nombre').value.trim();
        const email = $('#email').value.trim();
        const telefono = $('#telefono').value.trim();
        const direccion = $('#direccion').value.trim();
        if(!nombre) return;
        clientes.push({ nombre, email, telefono, direccion });
        save();
        render();
        form.reset();
    });

    table.addEventListener('click', event => {
        const button = event.target.closest('[data-index]');
        if(!button) return;
        clientes.splice(Number(button.dataset.index), 1);
        save();
        render();
    });

    load();
    render();
})();''',
    'clientes/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=clientes.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a clientes... <a href="clientes.html">clic aquí</a>.</p>
    <script>window.location.href = 'clientes.html';</script>
</body>

</html>''',
    'compras.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compras | Meier Distribuciones</title>
    <link rel="stylesheet" href="admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="auth.js"></script>

<div class="dashboard">

    <aside class="sidebar">

        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="dashboard.html">🏠 Dashboard</a>
            <a href="productos/productos.html">📦 Productos</a>
            <a href="ventas/ventas.html">🛒 Ventas</a>
            <a href="compras.html">🚚 Compras</a>
            <a href="proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="clientes/clientes.html">👥 Clientes</a>
            <a href="gastos/gastos.html">💰 Gastos</a>
            <a href="reportes.html">📈 Reportes</a>
            <a href="estadisticas/estadisticas.html">📊 Estadísticas</a>
            <a href="stock/index.html">📦 Stock</a>
            <a href="config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>

    </aside>

    <main>

        <h1>Compras</h1>

        <div class="cards">
            <div class="card">
                <h3>Total compras</h3>
                <h2 id="comprasTotal">0</h2>
            </div>
            <div class="card">
                <h3>Gasto total</h3>
                <h2 id="comprasValor">$0</h2>
            </div>
        </div>

        <section style="background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);margin-top:20px;">
            <h2>Registrar compra</h2>
            <form id="compraForm" style="display:grid;gap:14px;margin-top:18px;">
                <input type="text" id="producto" placeholder="Producto" required>
                <input type="text" id="proveedor" placeholder="Proveedor" required>
                <input type="number" id="cantidad" placeholder="Cantidad" min="1" value="1" required>
                <input type="number" id="precio" placeholder="Precio unitario" min="0" step="0.01" required>
                <input type="date" id="fecha" required>
                <textarea id="notas" rows="3" placeholder="Notas adicionales"></textarea>
                <button type="submit">Guardar compra</button>
            </form>
        </section>

        <section style="margin-top:30px;background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);">
            <h2>Historial de compras</h2>
            <div style="overflow-x:auto;margin-top:18px;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f6f7fb;">
                            <th style="padding:12px;text-align:left;">Producto</th>
                            <th style="padding:12px;text-align:left;">Proveedor</th>
                            <th style="padding:12px;text-align:left;">Cantidad</th>
                            <th style="padding:12px;text-align:left;">Precio</th>
                            <th style="padding:12px;text-align:left;">Fecha</th>
                            <th style="padding:12px;text-align:left;">Acción</th>
                        </tr>
                    </thead>
                    <tbody id="comprasTable">
                        <tr>
                            <td colspan="6" style="padding:18px;text-align:center;color:#6b7280;">No hay compras registradas.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

    </main>

</div>

<script src="compras.js"></script>

</body>

</html>''',
    'compras.js': '''(function(){
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
        table.innerHTML = compras.map((compra,index) => `\n            <tr>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.producto}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.proveedor}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.cantidad}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${new Intl.NumberFormat('es-AR',{style:'currency',currency:'ARS'}).format(compra.precio)}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${compra.fecha}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>\n            </tr>`).join('');
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
})();''',
    'config/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=config.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a configuración... <a href="config.html">clic aquí</a>.</p>
    <script>window.location.href = 'config.html';</script>
</body>

</html>''',
    'config/config.js': '''(function(){
    const STORAGE_KEY = 'meier_config';
    const $ = selector => document.querySelector(selector);
    const form = $('#configForm');
    const storeName = $('#storeName');
    const currency = $('#currency');
    const taxRate = $('#taxRate');
    const storeNotes = $('#storeNotes');

    function load(){
        try {
            const settings = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
            storeName.value = settings.storeName || '';
            currency.value = settings.currency || 'ARS';
            taxRate.value = settings.taxRate || '';
            storeNotes.value = settings.storeNotes || '';
        } catch {
            // ignore
        }
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        localStorage.setItem(STORAGE_KEY, JSON.stringify({
            storeName: storeName.value.trim(),
            currency: currency.value.trim() || 'ARS',
            taxRate: Number(taxRate.value) || 0,
            storeNotes: storeNotes.value.trim()
        }));
        alert('Configuración guardada');
    });

    load();
})();''',
    'productos/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=productos.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a productos... <a href="productos.html">clic aquí</a>.</p>
    <script>window.location.href = 'productos.html';</script>
</body>

</html>''',
    'productos/productos.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Productos | Meier Distribuciones</title>
    <link rel="stylesheet" href="../admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="../auth.js"></script>

<div class="dashboard">

    <aside class="sidebar">

        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="../dashboard.html">🏠 Dashboard</a>
            <a href="productos.html">📦 Productos</a>
            <a href="../ventas/ventas.html">🛒 Ventas</a>
            <a href="../compras.html">🚚 Compras</a>
            <a href="../proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="../clientes/clientes.html">👥 Clientes</a>
            <a href="../gastos/gastos.html">💰 Gastos</a>
            <a href="../reportes.html">📈 Reportes</a>
            <a href="../estadisticas/estadisticas.html">📊 Estadísticas</a>
            <a href="../stock/index.html">📦 Stock</a>
            <a href="../config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>

    </aside>

    <main>

        <h1>Productos</h1>

        <div class="cards">
            <div class="card">
                <h3>Total productos</h3>
                <h2 id="productosCount">0</h2>
            </div>
        </div>

        <section style="background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);margin-top:20px;">
            <h2>Agregar producto</h2>
            <form id="productoForm" style="display:grid;gap:14px;margin-top:18px;">
                <input type="text" id="prodNombre" placeholder="Nombre" required>
                <input type="text" id="prodMarca" placeholder="Marca">
                <input type="text" id="prodCategoria" placeholder="Categoría">
                <input type="number" id="prodPrecio" placeholder="Precio" min="0" step="0.01" required>
                <input type="number" id="prodStock" placeholder="Stock" min="0" value="0" required>
                <textarea id="prodDescripcion" rows="3" placeholder="Descripción"></textarea>
                <button type="submit">Guardar producto</button>
            </form>
        </section>

        <section style="margin-top:30px;background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);">
            <h2>Inventario</h2>
            <div style="overflow-x:auto;margin-top:18px;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f6f7fb;">
                            <th style="padding:12px;text-align:left;">Nombre</th>
                            <th style="padding:12px;text-align:left;">Marca</th>
                            <th style="padding:12px;text-align:left;">Categoría</th>
                            <th style="padding:12px;text-align:left;">Precio</th>
                            <th style="padding:12px;text-align:left;">Stock</th>
                            <th style="padding:12px;text-align:left;">Acción</th>
                        </tr>
                    </thead>
                    <tbody id="productosTable">
                        <tr>
                            <td colspan="6" style="padding:18px;text-align:center;color:#6b7280;">No hay productos registrados.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

    </main>

</div>

<script src="productos.js"></script>

</body>

</html>''',
    'productos/productos.js': '''(function(){
    const STORAGE_KEY = 'meier_productos';
    const $ = selector => document.querySelector(selector);
    const form = $('#productoForm');
    const table = $('#productosTable');
    const count = $('#productosCount');
    let products = [];

    function load(){
        try {
            products = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            products = [];
        }
    }

    function save(){
        localStorage.setItem(STORAGE_KEY, JSON.stringify(products));
    }

    function render(){
        count.textContent = products.length;
        if(!products.length){
            table.innerHTML = '<tr><td colspan="6" style="padding:18px;text-align:center;color:#6b7280;">No hay productos registrados.</td></tr>';
            return;
        }
        table.innerHTML = products.map((product,index) => `\n            <tr>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${product.nombre}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${product.marca||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${product.categoria||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${new Intl.NumberFormat('es-AR',{style:'currency',currency:'ARS'}).format(product.precio)}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${product.stock}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>\n            </tr>`).join('');
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        const nombre = $('#prodNombre').value.trim();
        const marca = $('#prodMarca').value.trim();
        const categoria = $('#prodCategoria').value.trim();
        const precio = Number($('#prodPrecio').value) || 0;
        const stockValue = Number($('#prodStock').value) || 0;
        if(!nombre) return;
        products.push({ nombre, marca, categoria, precio, stock: stockValue, descripcion: $('#prodDescripcion').value.trim() });
        save();
        render();
        form.reset();
    });

    document.addEventListener('click', event => {
        const button = event.target.closest('[data-index]');
        if(!button) return;
        products.splice(Number(button.dataset.index), 1);
        save();
        render();
    });

    load();
    render();
})();''',
    'proveedores/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=proveedores.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a proveedores... <a href="proveedores.html">clic aquí</a>.</p>
    <script>window.location.href = 'proveedores.html';</script>
</body>

</html>''',
    'proveedores/proveedores.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proveedores | Meier Distribuciones</title>
    <link rel="stylesheet" href="../admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="../auth.js"></script>

<div class="dashboard">
    <aside class="sidebar">
        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="../dashboard.html">🏠 Dashboard</a>
            <a href="../productos/productos.html">📦 Productos</a>
            <a href="../ventas/ventas.html">🛒 Ventas</a>
            <a href="../compras.html">🚚 Compras</a>
            <a href="../proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="../clientes/clientes.html">👥 Clientes</a>
            <a href="../gastos/gastos.html">💰 Gastos</a>
            <a href="../reportes.html">📈 Reportes</a>
            <a href="../estadisticas/estadisticas.html">📊 Estadísticas</a>
            <a href="../stock/index.html">📦 Stock</a>
            <a href="../config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>
    </aside>

    <main>
        <h1>Proveedores</h1>

        <div class="cards">
            <div class="card">
                <h3>Total proveedores</h3>
                <h2 id="proveedoresTotal">0</h2>
            </div>
        </div>

        <section style="background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);margin-top:20px;">
            <h2>Registrar proveedor</h2>
            <form id="proveedorForm" style="display:grid;gap:14px;margin-top:18px;">
                <input type="text" id="nombre" placeholder="Nombre" required>
                <input type="text" id="telefono" placeholder="Teléfono">
                <input type="text" id="direccion" placeholder="Dirección">
                <input type="text" id="contacto" placeholder="Contacto">
                <textarea id="observaciones" rows="3" placeholder="Observaciones"></textarea>
                <button type="submit">Guardar proveedor</button>
            </form>
        </section>

        <section style="margin-top:30px;background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);">
            <h2>Lista de proveedores</h2>
            <div style="overflow-x:auto;margin-top:18px;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f6f7fb;">
                            <th style="padding:12px;text-align:left;">Nombre</th>
                            <th style="padding:12px;text-align:left;">Teléfono</th>
                            <th style="padding:12px;text-align:left;">Dirección</th>
                            <th style="padding:12px;text-align:left;">Contacto</th>
                            <th style="padding:12px;text-align:left;">Acción</th>
                        </tr>
                    </thead>
                    <tbody id="proveedoresTable">
                        <tr>
                            <td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">No hay proveedores registrados.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
</div>

<script src="proveedores.js"></script>

</body>

</html>''',
    'proveedores/proveedores.js': '''(function(){
    const STORAGE_KEY = 'meier_proveedores';
    const $ = selector => document.querySelector(selector);
    const form = $('#proveedorForm');
    const table = $('#proveedoresTable');
    const total = $('#proveedoresTotal');
    let providers = [];

    function load(){
        try {
            providers = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            providers = [];
        }
    }

    function save(){
        localStorage.setItem(STORAGE_KEY, JSON.stringify(providers));
    }

    function render(){
        total.textContent = providers.length;
        if(!providers.length){
            table.innerHTML = '<tr><td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">No hay proveedores registrados.</td></tr>';
            return;
        }
        table.innerHTML = providers.map((provider,index) => `\n            <tr>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${provider.nombre}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${provider.telefono||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${provider.direccion||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${provider.contacto||'-'}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>\n            </tr>`).join('');
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        const nombre = $('#nombre').value.trim();
        const telefono = $('#telefono').value.trim();
        const direccion = $('#direccion').value.trim();
        const contacto = $('#contacto').value.trim();
        const observaciones = $('#observaciones').value.trim();
        if(!nombre) return;
        providers.push({ nombre, telefono, direccion, contacto, observaciones });
        save();
        render();
        form.reset();
    });

    table.addEventListener('click', event => {
        const button = event.target.closest('[data-index]');
        if(!button) return;
        providers.splice(Number(button.dataset.index), 1);
        save();
        render();
    });

    load();
    render();
})();''',
    'stock/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=stock.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a stock... <a href="stock.html">clic aquí</a>.</p>
    <script>window.location.href = 'stock.html';</script>
</body>

</html>''',
    'stock/stock.js': '''(function(){
    const STORAGE_KEY = 'meier_stock';
    const $ = selector => document.querySelector(selector);
    const form = $('#stockForm');
    const table = $('#stockTable');
    const total = $('#stockTotal');
    let items = [];

    function load(){
        try {
            items = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            items = [];
        }
    }

    function save(){
        localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    }

    function render(){
        total.textContent = items.reduce((sum,item) => sum + Number(item.cantidad), 0);
        if(!items.length){
            table.innerHTML = '<tr><td colspan="3" style="padding:18px;text-align:center;color:#6b7280;">No hay productos en stock.</td></tr>';
            return;
        }
        table.innerHTML = items.map((item,index) => `\n            <tr>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${item.producto}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${item.cantidad}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>\n            </tr>`).join('');
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        const producto = $('#item').value.trim();
        const cantidad = Number($('#cantidad').value) || 0;
        if(!producto) return;
        const existing = items.find(i => i.producto.toLowerCase() === producto.toLowerCase());
        if(existing){
            existing.cantidad += cantidad;
        } else {
            items.push({ producto, cantidad });
        }
        save();
        render();
        form.reset();
    });

    table.addEventListener('click', event => {
        const button = event.target.closest('[data-index]');
        if(!button) return;
        items.splice(Number(button.dataset.index), 1);
        save();
        render();
    });

    load();
    render();
})();''',
    'ventas/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=ventas.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a ventas... <a href="ventas.html">clic aquí</a>.</p>
    <script>window.location.href = 'ventas.html';</script>
</body>

</html>''',
    'ventas/ventas.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ventas | Meier Distribuciones</title>
    <link rel="stylesheet" href="../admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="../auth.js"></script>

<div class="dashboard">
    <aside class="sidebar">
        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="../dashboard.html">🏠 Dashboard</a>
            <a href="../productos/productos.html">📦 Productos</a>
            <a href="ventas.html">🛒 Ventas</a>
            <a href="../compras.html">🚚 Compras</a>
            <a href="../proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="../clientes/clientes.html">👥 Clientes</a>
            <a href="../gastos/gastos.html">💰 Gastos</a>
            <a href="../reportes.html">📈 Reportes</a>
            <a href="../estadisticas/estadisticas.html">📊 Estadísticas</a>
            <a href="../stock/index.html">📦 Stock</a>
            <a href="../config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>
    </aside>

    <main>
        <h1>Ventas</h1>

        <div class="cards">
            <div class="card">
                <h3>Total ventas</h3>
                <h2 id="ventasTotal">0</h2>
            </div>
            <div class="card">
                <h3>Ingresos</h3>
                <h2 id="ventasIngresos">$0</h2>
            </div>
        </div>

        <section style="background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);margin-top:20px;">
            <h2>Registrar venta</h2>
            <form id="ventasForm" style="display:grid;gap:14px;margin-top:18px;">
                <input type="text" id="producto" placeholder="Producto" required>
                <input type="number" id="cantidad" placeholder="Cantidad" min="1" value="1" required>
                <input type="number" id="precio" placeholder="Precio unitario" min="0" step="0.01" required>
                <input type="date" id="fecha" required>
                <textarea id="notas" rows="3" placeholder="Notas adicionales"></textarea>
                <button type="submit">Guardar venta</button>
            </form>
        </section>

        <section style="margin-top:30px;background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);">
            <h2>Historial de ventas</h2>
            <div style="overflow-x:auto;margin-top:18px;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f6f7fb;">
                            <th style="padding:12px;text-align:left;">Producto</th>
                            <th style="padding:12px;text-align:left;">Cantidad</th>
                            <th style="padding:12px;text-align:left;">Precio</th>
                            <th style="padding:12px;text-align:left;">Fecha</th>
                            <th style="padding:12px;text-align:left;">Acción</th>
                        </tr>
                    </thead>
                    <tbody id="ventasTable">
                        <tr>
                            <td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">No hay ventas registradas.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
</div>

<script src="ventas.js"></script>

</body>

</html>''',
    'ventas/ventas.js': '''(function(){
    const STORAGE_KEY = 'meier_ventas';
    const $ = selector => document.querySelector(selector);
    const form = $('#ventasForm');
    const table = $('#ventasTable');
    const total = $('#ventasTotal');
    const ingresos = $('#ventasIngresos');
    let ventas = [];

    function load(){
        try {
            ventas = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        } catch {
            ventas = [];
        }
    }

    function save(){
        localStorage.setItem(STORAGE_KEY, JSON.stringify(ventas));
    }

    function render(){
        total.textContent = ventas.length;
        const totalIngresos = ventas.reduce((sum, venta) => sum + Number(venta.cantidad) * Number(venta.precio), 0);
        ingresos.textContent = new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(totalIngresos);
        if(!ventas.length){
            table.innerHTML = '<tr><td colspan="5" style="padding:18px;text-align:center;color:#6b7280;">No hay ventas registradas.</td></tr>';
            return;
        }
        table.innerHTML = ventas.map((venta,index) => `\n            <tr>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${venta.producto}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${venta.cantidad}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${new Intl.NumberFormat('es-AR',{style:'currency',currency:'ARS'}).format(venta.precio)}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb">${venta.fecha}</td>\n                <td style="padding:12px;border-bottom:1px solid #e5e7eb"><button data-index="${index}" style="padding:8px 12px;border:none;border-radius:8px;background:#ef4444;color:#fff;cursor:pointer;">Eliminar</button></td>\n            </tr>`).join('');
    }

    form.addEventListener('submit', event => {
        event.preventDefault();
        const producto = $('#producto').value.trim();
        const cantidad = Number($('#cantidad').value) || 0;
        const precio = Number($('#precio').value) || 0;
        const fecha = $('#fecha').value;
        const notas = $('#notas').value.trim();
        if(!producto || !fecha) return;
        ventas.push({ producto, cantidad, precio, fecha, notas });
        save();
        render();
        form.reset();
    });

    table.addEventListener('click', event => {
        const button = event.target.closest('[data-index]');
        if(!button) return;
        ventas.splice(Number(button.dataset.index), 1);
        save();
        render();
    });

    load();
    render();
})();''',
    'estadisticas/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=estadisticas.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a estadísticas... <a href="estadisticas.html">clic aquí</a>.</p>
    <script>window.location.href = 'estadisticas.html';</script>
</body>

</html>''',
    'estadisticas/estadisticas.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estadísticas | Meier Distribuciones</title>
    <link rel="stylesheet" href="../admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="../auth.js"></script>

<div class="dashboard">
    <aside class="sidebar">
        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="../dashboard.html">🏠 Dashboard</a>
            <a href="../productos/productos.html">📦 Productos</a>
            <a href="../ventas/ventas.html">🛒 Ventas</a>
            <a href="../compras.html">🚚 Compras</a>
            <a href="../proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="../clientes/clientes.html">👥 Clientes</a>
            <a href="../gastos/gastos.html">💰 Gastos</a>
            <a href="../reportes.html">📈 Reportes</a>
            <a href="estadisticas.html">📊 Estadísticas</a>
            <a href="../stock/index.html">📦 Stock</a>
            <a href="../config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>
    </aside>

    <main>
        <h1>Estadísticas</h1>
        <div class="cards">
            <div class="card">
                <h3>Ventas totales</h3>
                <h2 id="statVentas">$0</h2>
            </div>
            <div class="card">
                <h3>Compras totales</h3>
                <h2 id="statCompras">$0</h2>
            </div>
            <div class="card">
                <h3>Gastos</h3>
                <h2 id="statGastos">$0</h2>
            </div>
            <div class="card">
                <h3>Clientes</h3>
                <h2 id="statClientes">0</h2>
            </div>
        </div>

        <section style="margin-top:30px;background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);">
            <h2>Resumen mensual</h2>
            <p id="monthSummary" style="color:#475569;line-height:1.7;margin-top:14px;">Los datos se calculan a partir de las ventas, compras y gastos registrados en el sistema.</p>
        </section>
    </main>
</div>

<script src="estadisticas.js"></script>

</body>

</html>''',
    'estadisticas/estadisticas.js': '''(function(){
    const getJSON = key => {
        try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch { return []; }
    };
    const ventas = getJSON('meier_ventas');
    const compras = getJSON('meier_compras');
    const gastos = getJSON('meier_gastos');
    const clientes = getJSON('meier_clientes');
    const format = value => new Intl.NumberFormat('es-AR', { style:'currency', currency:'ARS' }).format(value);
    const totalVentas = ventas.reduce((sum, v) => sum + Number(v.cantidad) * Number(v.precio), 0);
    const totalCompras = compras.reduce((sum, c) => sum + Number(c.cantidad) * Number(c.precio), 0);
    const totalGastos = gastos.reduce((sum, g) => sum + Number(g.monto), 0);
    document.getElementById('statVentas').textContent = format(totalVentas);
    document.getElementById('statCompras').textContent = format(totalCompras);
    document.getElementById('statGastos').textContent = format(totalGastos);
    document.getElementById('statClientes').textContent = clientes.length;
    document.getElementById('monthSummary').textContent = `Ingresos: ${format(totalVentas)}, compras: ${format(totalCompras)}, gastos: ${format(totalGastos)}. Clientes registrados: ${clientes.length}.`;
})();''',
    'reportes.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reportes | Meier Distribuciones</title>
    <link rel="stylesheet" href="admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

<script src="auth.js"></script>

<div class="dashboard">
    <aside class="sidebar">
        <div class="logoPanel">
            <h2>MEIER</h2>
            <p>DISTRIBUCIONES</p>
        </div>

        <nav>
            <a href="dashboard.html">🏠 Dashboard</a>
            <a href="productos/productos.html">📦 Productos</a>
            <a href="ventas/ventas.html">🛒 Ventas</a>
            <a href="compras.html">🚚 Compras</a>
            <a href="proveedores/proveedores.html">🏢 Proveedores</a>
            <a href="clientes/clientes.html">👥 Clientes</a>
            <a href="gastos/gastos.html">💰 Gastos</a>
            <a href="reportes.html">📈 Reportes</a>
            <a href="estadisticas/estadisticas.html">📊 Estadísticas</a>
            <a href="stock/index.html">📦 Stock</a>
            <a href="config/index.html">⚙ Configuración</a>
        </nav>

        <button id="logout">Cerrar sesión</button>
    </aside>

    <main>
        <h1>Reportes</h1>

        <section style="background:#fff;padding:28px;border-radius:20px;box-shadow:0 12px 30px rgba(0,0,0,.08);margin-top:20px;">
            <h2>Filtrar reportes</h2>
            <form id="reportForm" style="display:grid;gap:14px;margin-top:18px;max-width:520px;">
                <select id="reportType" required>
                    <option value="ventas">Ventas</option>
                    <option value="compras">Compras</option>
                    <option value="gastos">Gastos</option>
                    <option value="clientes">Clientes</option>
                    <option value="proveedores">Proveedores</option>
                </select>
                <input type="date" id="fromDate">
                <input type="date" id="toDate">
                <button type="submit">Generar reporte</button>
            </form>
            <div id="reportResult" style="margin-top:22px;color:#475569;"></div>
        </section>
    </main>
</div>

<script src="reportes.js"></script>

</body>

</html>''',
    'reportes.js': '''(function(){
    const $ = selector => document.querySelector(selector);
    const reportForm = $('#reportForm');
    const reportResult = $('#reportResult');
    const storageMap = {
        ventas: 'meier_ventas',
        compras: 'meier_compras',
        gastos: 'meier_gastos',
        clientes: 'meier_clientes',
        proveedores: 'meier_proveedores'
    };
    const parseJSON = key => {
        try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch { return []; }
    };
    const formatCurrency = value => new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(value);

    reportForm.addEventListener('submit', event => {
        event.preventDefault();
        const tipo = $('#reportType').value;
        const desde = $('#fromDate').value;
        const hasta = $('#toDate').value;
        let data = parseJSON(storageMap[tipo] || '[]');
        if(desde){ data = data.filter(item => item.fecha >= desde); }
        if(hasta){ data = data.filter(item => item.fecha <= hasta); }
        let message = '';
        if(tipo === 'ventas' || tipo === 'compras'){
            const total = data.reduce((sum, item) => sum + Number(item.cantidad) * Number(item.precio), 0);
            message = `<p>${data.length} registros. Total: ${formatCurrency(total)}</p>`;
        } else if(tipo === 'gastos'){
            const total = data.reduce((sum, item) => sum + Number(item.monto), 0);
            message = `<p>${data.length} registros. Total gastos: ${formatCurrency(total)}</p>`;
        } else {
            message = `<p>${data.length} registros.</p>`;
        }
        reportResult.innerHTML = message;
    });
})();''',
    'gastos/index.html': '''<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=gastos.html">
    <title>Redirigiendo...</title>
</head>

<body>
    <p>Redirigiendo a gastos... <a href="gastos.html">clic aquí</a>.</p>
    <script>window.location.href = 'gastos.html';</script>
</body>

</html>'''
}

for rel_path, content in FILES.items():
    target = base / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')
print(f'WROTE {len(FILES)} files')
