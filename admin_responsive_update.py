from pathlib import Path
import re

base = Path('admin')

common_css = '''body {
    background: #eef3f8;
    font-family: 'Poppins', sans-serif;
    color: #0f172a;
    margin: 0;
    min-height: 100vh;
}

main {
    padding: 40px;
    max-width: 1080px;
    margin: 0 auto;
}

h1 {
    margin-bottom: 24px;
    font-size: 2.2rem;
}

section {
    background: #fff;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 12px 30px rgba(0,0,0,.08);
    margin-top: 20px;
}

form {
    display: grid;
    gap: 14px;
    margin-top: 18px;
}

input,
select,
textarea {
    width: 100%;
    padding: 14px 16px;
    border-radius: 14px;
    border: 1px solid #d1d5db;
    background: #f8fafc;
    font-size: 15px;
    color: #0f172a;
}

textarea {
    min-height: 110px;
    resize: vertical;
}

button {
    width: fit-content;
    padding: 14px 26px;
    border: none;
    border-radius: 14px;
    background: #0e5db8;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
    transition: transform .2s ease, box-shadow .2s ease;
}

button:hover {
    transform: translateY(-1px);
    box-shadow: 0 14px 30px rgba(14,93,184,.2);
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 18px;
}

th,
td {
    padding: 14px 12px;
    border-bottom: 1px solid #e5e7eb;
    text-align: left;
}

thead tr {
    background: #f6f7fb;
}

tbody tr:hover {
    background: #f8fafc;
}

.empty-row td {
    color: #6b7280;
    text-align: center;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,.08);
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
}

@media(max-width: 860px) {
    main {
        padding: 24px;
    }
    section {
        padding: 22px;
        border-radius: 18px;
    }
    input,
    select,
    textarea,
    button {
        font-size: 14px;
    }
    h1 {
        font-size: 1.9rem;
    }
}

@media(max-width: 640px) {
    main {
        padding: 18px;
    }
    .cards {
        grid-template-columns: 1fr;
    }
    table,
    thead,
    tbody,
    th,
    td,
    tr {
        display: block;
        width: 100%;
    }
    thead {
        display: none;
    }
    tr {
        margin-bottom: 16px;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        overflow: hidden;
    }
    td {
        display: flex;
        justify-content: space-between;
        padding: 12px 14px;
        border: none;
        border-bottom: 1px solid #e5e7eb;
    }
    td:last-child {
        border-bottom: none;
    }
    td::before {
        content: attr(data-label);
        font-weight: 600;
        color: #475569;
        width: 40%;
        flex-shrink: 0;
    }
}
'''

reportes_css = '''body {
    background: #eef3f8;
    font-family: 'Poppins', sans-serif;
    color: #0f172a;
    margin: 0;
    min-height: 100vh;
}

main {
    padding: 40px;
    max-width: 1080px;
    margin: 0 auto;
}

h1 {
    margin-bottom: 24px;
    font-size: 2.2rem;
}

section {
    background: #fff;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 12px 30px rgba(0,0,0,.08);
    margin-top: 20px;
}

form {
    display: grid;
    gap: 14px;
    max-width: 520px;
    margin-top: 18px;
}

input,
select {
    width: 100%;
    padding: 14px 16px;
    border-radius: 14px;
    border: 1px solid #d1d5db;
    background: #f8fafc;
    font-size: 15px;
    color: #0f172a;
}

button {
    width: fit-content;
    padding: 14px 26px;
    border: none;
    border-radius: 14px;
    background: #0e5db8;
    color: #fff;
    font-weight: 600;
    cursor: pointer;
    transition: transform .2s ease;
}

button:hover {
    transform: translateY(-1px);
}

#reportResult {
    margin-top: 22px;
    color: #475569;
}

@media(max-width: 860px) {
    main { padding: 24px; }
    section { padding: 22px; }
}

@media(max-width: 640px) {
    main { padding: 18px; }
}
'''

admin_css_extra = '''

@media(max-width:1024px){
    .sidebar{width:220px;}
    main{padding:30px;}
}

@media(max-width:860px){
    .dashboard{flex-direction:column;height:auto;}
    .sidebar{width:100%;height:auto;position:relative;padding:20px;}
    .sidebar nav{flex-direction:row;flex-wrap:wrap;gap:10px;}
    .sidebar nav a{flex:1 1 calc(50% - 10px);text-align:center;}
    main{padding:24px;}
    .cards{grid-template-columns:repeat(auto-fit,minmax(180px,1fr));}
}

@media(max-width:640px){
    .sidebar{padding:16px;}
    .sidebar nav a{flex:1 1 100%;}
    main{padding:18px;}
    .card{padding:20px;}
}
'''

css_files = {
    'clientes/clientes.css': common_css,
    'compras.css': common_css,
    'config/config.css': common_css,
    'gastos/gastos.css': common_css,
    'productos/productos.css': common_css,
    'proveedores/proveedores.css': common_css,
    'stock/stock.css': common_css,
    'ventas/ventas.css': common_css,
    'estadisticas/estadisticas.css': common_css,
    'reportes/reportes.css': reportes_css,
}

for rel, content in css_files.items():
    p = base / rel
    p.write_text(content, encoding='utf-8')

admin_path = base / 'admin.css'
admin_text = admin_path.read_text(encoding='utf-8')
if admin_css_extra not in admin_text:
    admin_path.write_text(admin_text + admin_css_extra, encoding='utf-8')

html_paths = list(base.rglob('*.html'))
style_re = re.compile(r"\s*style\s*=\s*(\"[^\"]*\"|'[^']*')")
for path in html_paths:
    text = path.read_text(encoding='utf-8')
    new_text = style_re.sub('', text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')

print('Responsive styles applied and inline styles removed for', len(html_paths), 'HTML files.')
