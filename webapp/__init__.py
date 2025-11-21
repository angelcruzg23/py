import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
    app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET", "dev-secret-change-me")

    # Registrar blueprints
    from .controllers.auth import auth_bp
    from .controllers.profile import profile_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    # Configurar logging a archivo (logs/app.log), con rotación
    logs_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, "app.log")

    handler = RotatingFileHandler(log_path, maxBytes=1024 * 1024, backupCount=3, encoding="utf-8")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
    handler.setFormatter(formatter)

    # Añadir handler si no está ya presente
    if not any(isinstance(h, RotatingFileHandler) for h in app.logger.handlers):
        app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.logger.info("Aplicación inicializada, logging habilitado en %s", log_path)

    return app


__all__ = ["create_app"]
"""Paquete webapp: contiene la aplicación Flask del prototipo de login."""

from .app import create_app

__all__ = ["create_app"]
