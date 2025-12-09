# source/aurum/init_db.py

import sqlite3
import os

# Base directory of this file (aurum/)
BASE_DIR = os.path.dirname(__file__)

# Paths inside the aurum package
INSTANCE_DIR = "/app/instance"
DB_PATH = os.path.join(INSTANCE_DIR, "app.db")
SCHEMA_PATH = "/app/aurum/schema.sql"


def initialize_db():
    print("DB PATH:", DB_PATH)
    print("SCHEMA PATH:", SCHEMA_PATH)


    # Ensure instance directory exists
    os.makedirs(INSTANCE_DIR, exist_ok=True)

    # Skip if DB already exists
    if os.path.exists(DB_PATH):
        print("Database already exists. Skipping initialization.")
        return

    print("Database not found. Initializing...")

    conn = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_db()
