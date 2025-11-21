"""Wrapper script to run the Flask app using the app factory.

This runner reads PORT and HOST from environment variables so you can
override the default port (5001) to avoid conflicts with system services
(por ejemplo AirPlay que ocupa el puerto 5000 en macOS).
"""
import os
from . import create_app


def main():
    port = int(os.environ.get("PORT", os.environ.get("FLASK_PORT", "5001")))
    host = os.environ.get("HOST", "127.0.0.1")
    debug_env = os.environ.get("FLASK_DEBUG", os.environ.get("DEBUG", "1"))
    debug = str(debug_env).lower() in ("1", "true", "yes")

    app = create_app()
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()
