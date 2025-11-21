# Mi Proyecto Python

Este es un proyecto de ejemplo para aprender Python.

Estructura:

- `src/` - código fuente
- `tests/` - pruebas usando pytest
- `docs/` - documentación

Cómo empezar (zsh/macOS):

1. Crear y activar un entorno virtual:

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```zsh
pip install -r requirements.txt
```

3. Ejecutar el script de ejemplo:

```zsh
python -m src.main
```

4. Ejecutar pruebas:

```zsh
pip install pytest
pytest -q
```

Si quieres mover el proyecto a otra carpeta (por ejemplo tu repositorio), copia la carpeta `/tmp/mi_proyecto_python` a la ubicación deseada.
