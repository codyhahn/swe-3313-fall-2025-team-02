# source/shop.py
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
from aurum.db import get_db

shop_bp = Blueprint("shop", __name__)


@shop_bp.route("/home")
def home():
    return render_template("product.html")


@shop_bp.route("/shop")
def inventory():
    db = get_db()
    search = request.args.get("q", "").strip()
    if search:
        items = db.execute(
            """
            SELECT * FROM inventory
            WHERE is_sold = 0
              AND (title LIKE ? OR era LIKE ?)
            """,
            (f"%{search}%", f"%{search}%"),
        ).fetchall()
    else:
        items = db.execute(
            "SELECT * FROM inventory WHERE is_sold = 0"
        ).fetchall()
    return render_template("shop.html", items=items, search=search)


@shop_bp.route("/cart")
def cart():
    return render_template("cart.html")


# -------------------------------
#   API CART ENDPOINTS
# -------------------------------

from flask import jsonify

@shop_bp.route("/api/cart/add", methods=["POST"])
def api_cart_add():
    if "user_id" not in session:
        return jsonify({"error": "not logged in"}), 401

    data = request.get_json()
    inv_id = data.get("inventory_id")

    if not inv_id:
        return jsonify({"error": "missing inventory_id"}), 400

    db = get_db()

    try:
        db.execute(
            "INSERT OR IGNORE INTO cart_items (user_id, inventory_id) VALUES (?, ?)",
            (session["user_id"], inv_id),
        )
        db.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"success": True})


@shop_bp.route("/api/cart/count", methods=["GET"])
def api_cart_count():
    if "user_id" not in session:
        return jsonify({"count": 0})
    
    db = get_db()
    count = db.execute(
        "SELECT COUNT(*) FROM cart_items WHERE user_id = ?",
        (session["user_id"],)
    ).fetchone()[0]
    
    return jsonify({"count": count})


@shop_bp.route("/api/cart/contents", methods=["GET"])
def api_cart_contents():
    if "user_id" not in session:
        return jsonify({"items": []})

    db = get_db()
    items = db.execute(
        """
        SELECT inventory.id, title, era, price, image
        FROM cart_items
        JOIN inventory ON inventory.id = cart_items.inventory_id
        WHERE cart_items.user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    return jsonify({"items": [dict(i) for i in items]})

# REMOVE SINGLE ITEM FROM CART
@shop_bp.route("/api/cart/remove", methods=["POST"])
def api_cart_remove():
    if "user_id" not in session:
        return jsonify({"error": "not logged in"}), 401

    data = request.get_json()
    inv_id = data.get("inventory_id")

    if not inv_id:
        return jsonify({"error": "missing inventory_id"}), 400

    db = get_db()
    db.execute(
        "DELETE FROM cart_items WHERE user_id = ? AND inventory_id = ?",
        (session["user_id"], inv_id)
    )
    db.commit()

    return jsonify({"success": True})


# CLEAR ENTIRE CART
@shop_bp.route("/api/cart/clear", methods=["POST"])
def api_cart_clear():
    if "user_id" not in session:
        return jsonify({"error": "not logged in"}), 401

    db = get_db()
    db.execute("DELETE FROM cart_items WHERE user_id = ?", (session["user_id"],))
    db.commit()

    return jsonify({"success": True})







@shop_bp.route("/checkout")
def checkout():
    return render_template("checkout.html")



@shop_bp.route("/api/checkout", methods=["POST"])
def api_checkout():
    if "user_id" not in session:
        return jsonify({"error": "Not logged in"}), 401

    db = get_db()

    # LOAD CART ITEMS FROM DATABASE
    cart_items = db.execute(
        """
        SELECT inventory.id, inventory.title, inventory.era, inventory.price
        FROM cart_items
        JOIN inventory ON inventory.id = cart_items.inventory_id
        WHERE cart_items.user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    if not cart_items:
        return jsonify({"error": "Cart is empty"}), 400

    # CALCULATE TOTALS
    subtotal = sum(float(i["price"]) for i in cart_items)
    tax = round(subtotal * 0.06, 2)
    shipping = 10.00  # or any value you want from frontend
    total = round(subtotal + tax + shipping, 2)

    # CREATE ORDER
    cur = db.execute(
        """
        INSERT INTO orders (user_id, created_at, subtotal, tax, shipping, total)
        VALUES (?, datetime('now'), ?, ?, ?, ?)
        """,
        (session["user_id"], subtotal, tax, shipping, total)
    )
    order_id = cur.lastrowid

    # INSERT EACH PURCHASED ITEM + MARK SOLD
    for item in cart_items:
        db.execute(
            """
            INSERT INTO order_items (order_id, inventory_id, title, era, price)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                order_id,
                item["id"],
                item["title"],
                item["era"],
                item["price"]
            )
        )

        # Mark item as sold
        db.execute(
            "UPDATE inventory SET is_sold = 1 WHERE id = ?",
            (item["id"],)
        )

    # CLEAR CART
    db.execute("DELETE FROM cart_items WHERE user_id = ?", (session["user_id"],))
    db.commit()

    return jsonify({"order_id": order_id})


@shop_bp.route("/receipt/<int:order_id>")
def receipt(order_id):
    db = get_db()
    order = db.execute(
        "SELECT o.*, u.name AS customer_name "
        "FROM orders o JOIN users u ON o.user_id = u.id "
        "WHERE o.id = ?",
        (order_id,),
    ).fetchone()
    items = db.execute(
        "SELECT * FROM order_items WHERE order_id = ?",
        (order_id,),
    ).fetchall()

    if not order:
        return "Order not found", 404

    # Shape values for the template
    order_view = {
        "id": order["id"],
        "date": order["created_at"],
        "customer_name": order["customer_name"],
        "subtotal": order["subtotal"],
        "tax": order["tax"],
        "shipping": order["shipping"],
        "total": order["total"],
    }
    items_view = [
        {
            "name": i["title"],
            "era": i["era"],
            "price": i["price"],
        }
        for i in items
    ]

    return render_template("receipt.html", order=order_view, items=items_view)
