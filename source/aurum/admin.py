# source/admin.py
from flask import Blueprint, render_template, session, redirect, url_for
from aurum.db import get_db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/sales")
def sales_report():
    # Protect route: admin only
    if session.get("role") != "admin":
        return redirect(url_for("shop.home"))

    db = get_db()
    sales = db.execute(
        """
        SELECT o.id,
               o.created_at,
               u.name AS customer_name,
               o.total,
               o.shipping
        FROM orders o
        JOIN users u ON o.user_id = u.id
        ORDER BY o.created_at DESC
        """
    ).fetchall()

    # You can pass `sales` directly and loop in admin.html
    return render_template("admin.html", sales=sales)
