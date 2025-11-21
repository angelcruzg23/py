# Documentación mínima

Este documento explica cómo ejecutar el proyecto.

- Código fuente en `src/`.
- Pruebas en `tests/`.

Para ejecutar las pruebas correctamente desde la raíz del proyecto:

```zsh
cd /ruta/del/proyecto
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

Si pytest no encuentra el paquete `src`, ejecuta `PYTHONPATH=. pytest -q` o instala el paquete en modo editable:

```zsh
pip install -e .
```
