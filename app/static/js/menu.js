function renderMenu() {
    const header = document.getElementById('header-container');

    if (!token) {
        header.innerHTML = "";
        header.className = ""; // quitar estilos si no hay sesión
        return;
    }

    header.className = "header-biblio"; // aplicar clase al header principal
    header.innerHTML = `
        <div class="logo">
            <h1>📚 Fast-Libros</h1>
        </div>
        <nav class="menu">
            <ul>
                <li><a href="#" onclick="loadPage('main.html')">Inicio</a></li>
                <li><a href="#" onclick="loadPage('profile.html')">Perfil</a></li>
                <li><a href="#" onclick="loadPage('about.html')">Acerca de</a></li>
            </ul>
        </nav>
        <button onclick="logout()" class="logout-btn">Cerrar sesión</button>
    `;
}