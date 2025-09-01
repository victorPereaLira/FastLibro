// Función de login
async function login() {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    try {
        const response = await axios.post(`${AUTH_URL}/login`, {
            email: email,
            password: password
        });
        
        token = response.data.access_token;
        localStorage.setItem('token', token);
        checkAuth();
        document.getElementById('login-error').textContent = '';
    } catch (error) {
        document.getElementById('login-error').textContent = 
            error.response?.data?.detail || 'Credenciales incorrectas';
    }
}

// Función de registro
async function register() {
    const name = document.getElementById('register-name').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    
    try {
        await axios.post(`${AUTH_URL}/registro`, {
            nombre: name,
            email: email,
            password: password
        });
        
        document.getElementById('register-error').textContent = '';
        loadPage('login.html');
    } catch (error) {
        document.getElementById('register-error').textContent = 
            error.response?.data?.detail || 'Error al registrar';
    }
}

// Función de logout
function logout() {
    token = null;
    localStorage.removeItem('token');
    checkAuth();
}