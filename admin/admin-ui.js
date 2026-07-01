(function(){
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;

  const path = window.location.pathname.replace(/\/\/$/, '');
  const adminIndex = path.lastIndexOf('/admin/');
  const currentAdminPath = adminIndex !== -1 ? path.slice(adminIndex + 7) : path;
  const depth = currentAdminPath.split('/').length - 1; // file path includes file name
  const basePrefix = depth > 0 ? '../'.repeat(depth) : '';

  const standardSidebarHTML = `
    <div class="sidebar-top">
      <div class="logoPanel">
        <h2>MEIER</h2>
        <p>ERP PRO</p>
      </div>
      <nav>
        <a href="${basePrefix}dashboard.html">🏠 Dashboard</a>
        <a href="${basePrefix}ventas/ventas.html">🛒 Ventas</a>
        <a href="${basePrefix}productos/productos.html">📦 Productos</a>
        <a href="${basePrefix}clientes/clientes.html">👥 Clientes</a>
        <a href="${basePrefix}proveedores/proveedores.html">🏢 Proveedores</a>
        <a href="${basePrefix}compras/compras.html">🚚 Compras</a>
        <a href="${basePrefix}stock/stock.html">📦 Stock</a>
        <a href="${basePrefix}gastos/gastos.html">💰 Gastos</a>
        <a href="${basePrefix}estadisticas/estadisticas.html">📊 Estadísticas</a>
        <a href="${basePrefix}reportes.html">📈 Reportes</a>
        <a href="${basePrefix}config/config.html">⚙️ Configuración</a>
      </nav>
    </div>
    <div class="sidebar-bottom">
      <div class="user-card">
        <div class="user-avatar">M</div>
        <div class="user-info">
          <h4>Administrador</h4>
          <span>Panel administrativo</span>
        </div>
      </div>
      <button id="logout" type="button" class="btn btn-danger w100">Cerrar sesión</button>
    </div>
  `;

  sidebar.innerHTML = standardSidebarHTML;

  const existingToggle = document.querySelector('.menu-toggle');
  const existingBackdrop = document.querySelector('.sidebar-backdrop');

  const toggle = existingToggle || document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'menu-toggle';
  toggle.setAttribute('aria-label', 'Abrir menú de navegación');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-controls', 'sidebar');
  toggle.innerHTML = '<span></span><span></span><span></span>';

  const backdrop = existingBackdrop || document.createElement('div');
  backdrop.className = 'sidebar-backdrop';
  backdrop.tabIndex = -1;

  if (!existingToggle) document.body.appendChild(toggle);
  if (!existingBackdrop) document.body.appendChild(backdrop);

  if (!sidebar.id) {
    sidebar.id = 'sidebar';
  }

  const currentPathName = window.location.pathname.replace(/\/\/$/, '');

  sidebar.querySelectorAll('nav a').forEach((link) => {
    const href = link.getAttribute('href') || '';
    const normalizedHref = new URL(href, window.location.origin + currentPathName).pathname.replace(/\/\/$/, '');
    if (normalizedHref === currentPathName) {
      link.classList.add('active');
    }
  });

  const logoutButton = sidebar.querySelector('#logout');
  if (logoutButton) {
    logoutButton.addEventListener('click', () => {
      if (window.Auth && typeof window.Auth.cerrarSesion === 'function') {
        window.Auth.cerrarSesion();
      } else {
        window.location.replace(`${basePath}login.html`);
      }
    });
  }

  function closeSidebar(){
    sidebar.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    backdrop.classList.remove('active');
  }

  function openSidebar(){
    sidebar.classList.add('open');
    toggle.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    backdrop.classList.add('active');
  }

  toggle.addEventListener('click', () => {
    const isOpen = sidebar.classList.toggle('open');
    toggle.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    backdrop.classList.toggle('active', isOpen);
  });

  backdrop.addEventListener('click', closeSidebar);

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  });

  sidebar.querySelectorAll('a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.trim() !== '#') {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 1024) closeSidebar();
      });
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 1024) {
      closeSidebar();
    }
  });
})();
