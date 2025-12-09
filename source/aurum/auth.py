# source/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from aurum.db import get_db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/landing")
def landing():
    # index/login/hero page (templates/index.html)
    return render_template("index.html")


@auth_bp.route("/register", methods=["POST"])
def register():
    name = request.form.get("signup-name")
    email = request.form.get("signup-email")
    password = request.form.get("signup-password")

    if not name or not email or not password:
        flash("All fields are required for registration.")
        return redirect(url_for("auth.landing"))

    db = get_db()
    try:
        cursor = db.execute(
            "INSERT INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
            (name, email, generate_password_hash(password), "user"),
        )
        db.commit()

        # Auto-login user right after registration
        session.clear()
        session["user_id"] = cursor.lastrowid
        session["user_name"] = name
        session["role"] = "user"

        # Redirect to shop homepage
        return redirect(url_for("shop.home"))

    except Exception:
        flash("Email already in use.")
        return redirect(url_for("auth.landing"))



@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("signin-email")
    password = request.form.get("signin-password")

    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()

    if user and check_password_hash(user["password_hash"], password):
        session.clear()
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        session["role"] = user["role"]
        return redirect(url_for("shop.home"))

    flash("Invalid email or password.")
    return redirect(url_for("auth.landing"))


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.landing"))
