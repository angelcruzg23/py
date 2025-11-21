from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from webapp.models.users import validate_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET"])
def index():
    error = session.pop("login_error", None)
    return render_template("login.html", error=error)


@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    # Log del intento de login (no almacenamos la contraseña en claro)
    pw_len = len(password or "")
    current_app.logger.info("Login attempt: user=%s password_length=%d", username, pw_len)

    if validate_user(username, password):
        session["user"] = username
        current_app.logger.info("Login success: user=%s", username)
        return redirect(url_for("profile.view_profile"))
    else:
        current_app.logger.warning("Login failed: user=%s", username)
        session["login_error"] = "Usuario o contraseña incorrectos. Intenta de nuevo."
        return redirect(url_for("auth.index"))


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.index"))
