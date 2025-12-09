# Implementation - Aurum Gallery Application

This document provides detailed instructions for configuring, initializing, and running the Aurum Gallery Application. It is designed so the evaluator can launch the application from a terminal on any operating system, including macOS (M-series), without relying on an IDE.

---

## Environment Setup

### 1. Install Docker Desktop (Required)

The application runs entirely inside Docker. No local Python, Flask, SQLite, or virtual environment setup is required.

Download Docker Desktop:  
https://www.docker.com/products/docker-desktop/

After installation, verify Docker is available:

```bash
docker --version
docker compose version
```

Both commands should print version numbers with no errors.

---

### 2. Clone the Repository

```bash
git clone <https://github.com/codyhahn/swe-3313-fall-2025-team-02.git>
cd "SWE-3313 Project"
```

---

### 3. Verify Directory Structure

Your project root should contain:

```
swe-3313-fall-2025-team-02/
│
├── implementation/
│
├── project-plan/
│
├── requirements/
│
├── source/
│   │
│   ├── aurum/
│   │   ├── static/
│   │   │   ├── css/
│   │   │   ├── images/
│   │   │   └── js/
│   │   │
│   │   ├── templates/
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── app.py
│   │   ├── auth.py
│   │   ├── db.py
│   │   ├── init_db.py
│   │   ├── schema.sql
│   │   └── shop.py
│   │   
│   ├── .gitignore
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── env.example
│   └── requirements.txt
│
├── technical-design/
│
└── README.md

```

---

### 4. Environment Variables

The application uses a single environment variable:

```
SECRET_KEY=changeme
```

This is automatically loaded inside Docker.

---

## Data Storage Setup (SQLite Auto-Initialization)

The Aurum Gallery Application uses SQLite.  
**No manual setup is required.**

When you run:

```bash
docker compose up --build
```
The container will automatically:

1. Create the `aurum/instance/` directory if it does not already exist
2. Check whether `instance/app.db` exists
3. If the database is missing:
   - Create `app.db`
   - Run `init_db.py`
   - Execute all SQL commands in `schema.sql`
   - Seed the admin account, regular user account, and inventory data
4. If `app.db` already exists, initialization is skipped

The database is stored locally at:

```
source/instance/app.db
```

This directory is mounted as a Docker volume so the DB persists across restarts.

### Seeded Accounts

| Role            | Email               | Password |
|-----------------|---------------------|----------|
| Administrator   | admin@example.com   | admin123 |
| User            | user@example.com    | user123  |

---

## How to Start and Login

### 1. Build the Application

```bash
docker compose build
```

This installs dependencies and prepares the Flask environment inside the container.

---

### 2. Start the Application

```bash
docker compose up
```

First-time startup should show something like:

```
Database not found. Initializing...
Database initialized.
 * Running on http://0.0.0.0:5000
```

---

### 3. Open the Application in a Browser

Landing Page (login/register):

```
http://localhost:5000/landing
```

---

### 4. Login Credentials

| Role            | Email               | Password |
|-----------------|---------------------|----------|
| Administrator   | admin@example.com   | admin123 |
| User            | user@example.com    | user123  |

---

### 5. Post-Login Navigation

After login, users are redirected to:

```
http://localhost:5000/home
```

Administrators will see additional admin-only features.

---

### 6. Stopping the Application

```
CTRL + C
docker compose down
```

---

## Troubleshooting

### 1. Database changes not appearing in VS Code

**Cause:** The database was created inside the container before the host volume mounted. 
- **Fix:**

```bash
docker compose down
rm instance/app.db
docker compose up --build
```

This forces a full DB rebuild using `schema.sql`.

---

### 2. Port 5000 already in use

**macOS/Linux:**

```bash
lsof -i :5000
kill -9 <PID>
```

**Windows PowerShell:**

```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

Restart the app:

```bash
docker compose up
```

---

### 3. Docker not recognized

Restart your terminal or computer after installing Docker Desktop.

Verify installation:

```bash
docker --version
docker compose version
```

---

### 4. Import errors (e.g., “attempted relative import…”)

All imports are absolute to support running Flask as a script:

```python
from db import get_db
from auth import auth_bp
from shop import shop_bp
from admin import admin_bp
```

Ensure no `from .module import ...` statements remain (should be fixed but just in case).

---

### 5. Missing dependencies

All dependencies are installed inside the Docker image during:

```bash
docker compose build
```

Dependencies live in:

```
source/requirements.txt
```

---
To build, initialize, and run the app, the evaluator only needs to run:

```bash
docker compose up --build
```

Then open:

```
http://localhost:5000/landing
```

No IDE required.  
No Python installation required.  
No manual database setup required.  
Cross-platform and evaluator-friendly.


