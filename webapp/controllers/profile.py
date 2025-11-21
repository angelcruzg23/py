from flask import Blueprint, render_template, request, redirect, url_for, session
from webapp.models.profiles import load_user_data, save_user_data

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


@profile_bp.route("/", methods=["GET", "POST"])
def view_profile():
    if "user" not in session:
        session["login_error"] = "Debes iniciar sesión primero."
        return redirect(url_for("auth.index"))

    username = session.get("user")
    submitted = False
    data = load_user_data(username) or {}

    if request.method == "POST":
        data = {
            "nombres": request.form.get("nombres", "").strip(),
            "id_number": request.form.get("id_number", "").strip(),
            "direccion": request.form.get("direccion", "").strip(),
            "telefono": request.form.get("telefono", "").strip(),
            "pais": request.form.get("pais", "").strip(),
        }
        save_user_data(username, data)
        submitted = True

    return render_template("profile.html", user=username, submitted=submitted, data=data)
