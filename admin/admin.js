(function(){
  const $ = s => document.querySelector(s);
  const fmt = n => "$" + Number(n).toLocaleString("es-AR");
  const D = window.MEIER_DATA;
  let products = [...D.products];
  let editingId = null;

  const SESSION_KEY = "meier_admin_demo";
  function showDashboard(){
    $("#login").classList.add("hidden");
    $("#dashboard").classList.remove("hidden");
    renderAll();
  }
  if (sessionStorage.getItem(SESSION_KEY) === "1") showDashboard();

  $("#loginForm").addEventListener("submit", e => {
    e.preventDefault();
    const f = e.target;
    if (!f.checkValidity()){ f.reportValidity(); return; }
    const { user, pass } = Object.fromEntries(new FormData(f).entries());
    if (user === "admin" && pass === "admin"){
      sessionStorage.setItem(SESSION_KEY, "1");
      showDashboard();
    } else {
      alert("Credenciales inválidas. (demo: admin / admin)");
    }
  });
  $("#logout").addEventListener("click", () => {
    sessionStorage.removeItem(SESSION_KEY);
    location.reload();
  });

  let query = "";
  $("#adminSearch").addEventListener("input", e => { query = e.target.value.toLowerCase(); renderGrid(); });

  function renderAll(){ renderStats(); renderGrid(); }

  function renderStats(){
    const brands = new Set(products.map(p => p.brand));
    const cats = new Set(products.map(p => p.category));
    const value = products.reduce((s,p) => s + Number(p.price), 0);
    $("#sProducts").textContent = products.length;
    $("#sBrands").textContent = brands.size;
    $("#sCats").textContent = cats.size;
    $("#sValue").textContent = fmt(value);
  }
  function renderGrid(){
    const list = products.filter(p =>
      !query || p.name.toLowerCase().includes(query) || p.brand.toLowerCase().includes(query)
    );
    const grid = $("#adminGrid");
    if (!list.length){
      grid.innerHTML = `<div class="adminGrid__empty">Sin productos.</div>`;
      return;
    }
    grid.innerHTML = list.map(p => `
      <article class="acard">
        <div class="acard__img"><img src="${p.image}" alt="${p.name}" loading="lazy" onerror="this.style.display='none'"/></div>
        <div class="acard__body">
          <span class="acard__brand">${p.brand}</span>
          <h4 class="acard__name">${p.name}</h4>
          <div class="acard__meta">
            <span class="acard__cat">${p.category}</span>
            <span class="acard__price">${fmt(p.price)}</span>
          </div>
          <div class="acard__actions">
            <button class="btn-sm" data-edit="${p.id}" title="Editar producto">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z"/></svg>
              Editar
            </button>
            <button class="btn-sm danger" data-del="${p.id}" title="Eliminar producto">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m3 0v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/></svg>
            </button>
          </div>
        </div>
      </article>`).join("");
  }
  $("#adminGrid").addEventListener("click", e => {
    const btn = e.target.closest("button"); if (!btn) return;
    const ed = btn.dataset.edit, del = btn.dataset.del;
    if (ed) openModal(products.find(p => p.id === +ed));
    if (del && confirm("¿Eliminar producto?")){
      products = products.filter(p => p.id !== +del); renderAll();
    }
  });

  const modal = $("#prodModal");
  function openModal(p){
    editingId = p ? p.id : null;
    $("#prodTitle").textContent = p ? "Editar producto" : "Nuevo producto";
    const f = $("#prodForm");
    f.reset();
    if (p){ f.name.value=p.name; f.brand.value=p.brand; f.category.value=p.category; f.price.value=p.price; f.image.value=p.image||""; }
    modal.classList.add("open");
  }
  function closeModal(){ modal.classList.remove("open"); }
  $("#openNew").addEventListener("click", () => openModal(null));
  $("#prodClose").addEventListener("click", closeModal);
  modal.addEventListener("click", e => { if (e.target === modal) closeModal(); });

  $("#prodForm").addEventListener("submit", e => {
    e.preventDefault();
    const f = e.target;
    if (!f.checkValidity()){ f.reportValidity(); return; }
    const data = Object.fromEntries(new FormData(f).entries());
    data.price = +data.price;
    if (editingId){
      products = products.map(p => p.id === editingId ? { ...p, ...data } : p);
    } else {
      const id = Math.max(0, ...products.map(p => p.id)) + 1;
      products.push({ id, image: data.image || "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=500&q=80", ...data });
    }
    closeModal(); renderAll();
  });
})();