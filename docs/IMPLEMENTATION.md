# Implementación del prototipo de login (sin DB)

Este documento explica la estructura de archivos, las APIs creadas y el flujo de trabajo del prototipo implementado.

Estructura principal añadida

- `webapp/`
  - `__init__.py` - exporta `create_app`.
  - `app.py` - contiene la aplicación Flask y las rutas.
  - `templates/`
    - `login.html` - formulario de login (usuario, contraseña).
    - `profile.html` - formulario de datos personales y vista de datos enviados.
- `data/`
  - `users.txt` - archivo con usuarios y contraseñas en texto plano (prototipo): `usuario:contraseña`.

APIs / Rutas

- GET `/` -> página de login (muestra error si existe en sesión).
- POST `/login` -> procesa las credenciales. Si coinciden con `data/users.txt`, se guarda `session['user']` y redirige a `/profile`. Si fallan, vuelve a `/` con mensaje de error.
- GET, POST `/profile` -> requiere sesión; muestra formulario de datos personales (nombres, id, dirección, teléfono, país). POST procesa y muestra los datos enviados.
- GET `/logout` -> borra la sesión y vuelve al login.

Notas sobre la validación de usuarios

- Por ahora la validación es simple: el archivo `data/users.txt` tiene líneas `usuario:contraseña` en texto plano. La función `load_users()` lee este archivo y `validate_user()` compara usuario/contraseña exactamente.
- En el futuro se debe usar hashing (por ejemplo `werkzeug.security.generate_password_hash` / `check_password_hash`) y/o una base de datos.

Ejecución local (desarrollo)

1. Crear y activar un entorno virtual (recomendado):

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```zsh
pip install -r requirements.txt
```

3. Ejecutar la app (desde la raíz del proyecto):

```zsh
# opción A (usando Flask CLI):
export FLASK_APP=webapp.app
flask run

# opción B (directo con python):
python -m webapp.app
```

4. Abrir en el navegador: http://127.0.0.1:5000

Credenciales de ejemplo en `data/users.txt`:

- `alice:password123`
- `bob:secret`

Flujo de trabajo después del despliegue

- El usuario abre `/` y se autentica.
- Si las credenciales son correctas, accede a `/profile` donde rellena sus datos personales.
- Si falla, permanece en la página de login con un mensaje de error.

Siguientes pasos recomendados (seguridad y mejoras)

1. No guardar contraseñas en texto plano; usar hashing (`werkzeug.security`).
2. Mover la gestión de usuarios a una base de datos o archivo JSON con permisos adecuados.
3. Añadir validación y sanitización de los campos del perfil.
4. Usar HTTPS (TLS) y configurar secret key segura por variable de entorno.
5. Añadir tests (unitarios / funcionales) para la validación de login y el flujo de perfil.


*** Fin del documento
