# source/app.py
import os
from flask import Flask, redirect, url_for

from dotenv import load_dotenv
load_dotenv()

from aurum.db import init_db, close_db




def create_app():
    app = Flask(__name__, instance_path="/app/instance")

    # Config
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-change-me"),
        DATABASE=os.path.join(app.instance_path, "app.db"),
        
    )
    print("DB PATH:", app.config["DATABASE"])


    # Make sure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # DB teardown
    app.teardown_appcontext(close_db)

    # CLI: flask --app app:create_app init-db
    @app.cli.command("init-db")
    def init_db_command():
        """Initialize the database (tables + seed data)."""
        init_db()
        print("Initialized the database.")

    # Register blueprints
    from aurum.auth import auth_bp
    from aurum.shop import shop_bp
    from aurum.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(admin_bp)

    # Default route -> landing/login page
    @app.route("/")
    def index():
        return redirect(url_for("auth.landing"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)

