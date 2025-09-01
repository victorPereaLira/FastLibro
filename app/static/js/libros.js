// Configurar formulario de libro
function setupLibroForm() {
    const form = document.getElementById('form-libro');
    if (form) {
        form.onsubmit = async (e) => {
            e.preventDefault();
            await guardarLibro();
        };
    }
}

// Guardar nuevo libro
async function guardarLibro() {
    const libro = {
        titulo: document.getElementById('titulo').value,
        autor: document.getElementById('autor').value,
        genero: document.getElementById('genero').value,
        anio_publicacion: document.getElementById('anio').value ? 
                          parseInt(document.getElementById('anio').value) : null
    };
    
    try {
        await axios.post(API_URL, libro);
        cargarLibros();
        document.getElementById('form-libro').reset();
    } catch (error) {
        if (error.response?.status === 401) {
            logout();
        }
        console.error('Error al guardar libro:', error);
    }
}

// Cargar libros
async function cargarLibros() {
    try {
        const response = await axios.get(API_URL);
        mostrarLibros(response.data);
    } catch (error) {
        if (error.response?.status === 401) {
            logout();
        }
        console.error('Error al cargar libros:', error);
    }
}

// Mostrar libros en la lista
function mostrarLibros(libros) {
    const listado = document.querySelector('.libro-list');
    if (listado) {
        let html = '';
        libros.forEach(libro => {
            html += `
                <li class="libro-item">
                    <div>
                        <strong>${libro.titulo}</strong> - ${libro.autor}
                        ${libro.genero ? `<br><small>Género: ${libro.genero}</small>` : ''}
                        ${libro.anio_publicacion ? `<br><small>Año: ${libro.anio_publicacion}</small>` : ''}
                    </div>
                    <button class="delete-btn" onclick="eliminarLibro(${libro.id})">
                        Eliminar
                    </button>
                </li>
            `;
        });
        listado.innerHTML = html || '<li>No tienes libros guardados</li>';
    }
}

// Eliminar libro
async function eliminarLibro(id) {
    if (confirm('¿Estás seguro de que quieres eliminar este libro?')) {
        try {
            await axios.delete(`${API_URL}/${id}`);
            cargarLibros();
        } catch (error) {
            if (error.response?.status === 401) {
                logout();
            }
            console.error('Error al eliminar libro:', error);
        }
    }
}