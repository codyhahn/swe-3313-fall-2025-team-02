# Technical Design

## Table of Contents
- [Implementation Language(s)](#implementation-languages)
- [Implementation Framework(s)](#implementation-frameworks)
- [Data Storage Plan](#data-storage-plan)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Entity/Field Descriptions](#entityfield-descriptions)
- [Data Examples](#data-examples)
- [Database Seed Data](#database-seed-data)
- [Authentication and Authorization Plan](#authentication-and-authorization-plan)
- [Coding Style Guide](#coding-style-guide)
- [Presentation](#presentation)

---

## Implementation Language(s)

Our project is implemented primarily in:

- **Python 3.x**
  - Backend logic using Flask
  - Routing, input validation, and business rules
  - Database access and data manipulation

- **HTML5, CSS, JavaScript**
  - Frontend templates using Jinja2
  - Styling and layout for all pages
  - Basic interactivity and form handling

### Why we selected these languages

- **Python**
  - Easy to write and maintain
  - Fast development cycle for academic projects
  - Strong ecosystem for web apps
  - Documentation: https://docs.python.org/3/

- **HTML/CSS/JavaScript**
  - Standard for web UI
  - Works seamlessly with Flask templates
  - Documentation:
    - HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
    - CSS: https://developer.mozilla.org/en-US/docs/Web/CSS
    - JS: https://developer.mozilla.org/en-US/docs/Web/JavaScript

---

## Implementation Framework(s)

- **Flask**
  - Lightweight Python web framework
  - Handles routing, templating, and sessions
  - Documentation: https://flask.palletsprojects.com/

- **Jinja2**
  - Templating engine used by Flask
  - Supports template inheritance and clean UI patterns
  - Documentation: https://jinja.palletsprojects.com/

- **SQLite**
  - Simple file-based SQL database
  - Persistent and easy to deploy for the project
  - Documentation: https://www.sqlite.org/docs.html

### Why we selected these frameworks

- Simple learning curve compared to larger frameworks
- Excellent for rapid prototyping and semester-long projects
- Integrates cleanly with Python
- Zero configuration required for database setup

---

## Data Storage Plan

The application uses **SQL (SQLite)** for persistent storage.

We will:

- Store data in a single SQLite database: `app.db`
- Use the `sqlite3` Python library for database access
- Persist data across application restarts
- Use SQL constraints to protect data integrity  
  - Primary keys  
  - Foreign keys  
  - NOT NULL fields

### Tables used:

- `users`
- `categories`
- `products`
- `carts`
- `cart_items`
- `orders`
- `order_items`

---

## Entity Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ CART : "owns"
    USER ||--o{ ORDER : "places"
    CATEGORY ||--o{ PRODUCT : "categorizes"
    PRODUCT ||--o{ CART_ITEM : "appears_in"
    PRODUCT ||--o{ ORDER_ITEM : "appears_in"
    CART ||--o{ CART_ITEM : "contains"
    ORDER ||--o{ ORDER_ITEM : "contains"

    USER {
        int id
        string email
        string password_hash
        string first_name
        string last_name
        string role
        datetime created_at
    }

    CATEGORY {
        int id
        string name
        string description
    }

    PRODUCT {
        int id
        string name
        string description
        real price
        int stock_quantity
        int category_id
        string image_url
        datetime created_at
        boolean is_active
    }

    CART {
        int id
        int user_id
        datetime created_at
        datetime updated_at
    }

    CART_ITEM {
        int id
        int cart_id
        int product_id
        int quantity
        real unit_price_at_add
    }

    ORDER {
        int id
        int user_id
        real subtotal
        real tax_amount
        real shipping_amount
        real total_amount
        string status
        string shipping_address
        string billing_address
        datetime created_at
    }

    ORDER_ITEM {
        int id
        int order_id
        int product_id
        int quantity
        real unit_price
        real line_total
    }
```
## Entity/Field Descriptions

# User
| Field         | SQL Type | Example / Size     | Required | Key         | Description           |
| ------------- | -------- | ------------------ | -------- | ----------- | --------------------- |
| id            | INTEGER  | 32-bit             | Yes      | Primary Key | Unique user ID        |
| email         | TEXT     | 100 chars          | Yes      | Unique      | Login email           |
| password_hash | TEXT     | 255 chars          | Yes      |             | Hashed password       |
| first_name    | TEXT     | 50 chars           | Yes      |             | First name            |
| last_name     | TEXT     | 50 chars           | Yes      |             | Last name             |
| role          | TEXT     | `admin`/`customer` | Yes      |             | Authorization role    |
| created_at    | DATETIME | timestamp          | Yes      |             | Account creation time |


# Category
| Field       | SQL Type | Size | Required | Key         | Description          |
| ----------- | -------- | ---- | -------- | ----------- | -------------------- |
| id          | INTEGER  |      | Yes      | Primary Key | Unique category ID   |
| name        | TEXT     | 50   | Yes      | Unique      | Category name        |
| description | TEXT     | 255  | No       |             | Optional description |


# Product
| Field          | SQL Type | Size | Required | Key         | Description              |
| -------------- | -------- | ---- | -------- | ----------- | ------------------------ |
| id             | INTEGER  |      | Yes      | Primary Key | Product ID               |
| name           | TEXT     | 100  | Yes      |             | Product name             |
| description    | TEXT     | 1000 | Yes      |             | Detailed description     |
| price          | REAL     |      | Yes      |             | Product price            |
| stock_quantity | INTEGER  |      | Yes      |             | Inventory count          |
| category_id    | INTEGER  |      | Yes      | Foreign Key | References `CATEGORY.id` |
| image_url      | TEXT     | 255  | No       |             | Image path               |
| created_at     | DATETIME |      | Yes      |             | Added date               |
| is_active      | INTEGER  | 0/1  | Yes      |             | Whether item is active   |


# Cart
| Field      | SQL Type | Required | Key         | Description          |
| ---------- | -------- | -------- | ----------- | -------------------- |
| id         | INTEGER  | Yes      | Primary Key | Cart ID              |
| user_id    | INTEGER  | Yes      | Foreign Key | References `USER.id` |
| created_at | DATETIME | Yes      |             | Time created         |
| updated_at | DATETIME | Yes      |             | Last update          |


# Cart_Item
| Field             | SQL Type | Required | Key         | Description               |
| ----------------- | -------- | -------- | ----------- | ------------------------- |
| id                | INTEGER  | Yes      | Primary Key | Cart item ID              |
| cart_id           | INTEGER  | Yes      | Foreign Key | References `CART.id`      |
| product_id        | INTEGER  | Yes      | Foreign Key | References `PRODUCT.id`   |
| quantity          | INTEGER  | Yes      |             | Quantity                  |
| unit_price_at_add | REAL     | Yes      |             | Price snapshot when added |

#Order
| Field            | SQL Type | Required | Key         | Description          |
| ---------------- | -------- | -------- | ----------- | -------------------- |
| id               | INTEGER  | Yes      | Primary Key | Order ID             |
| user_id          | INTEGER  | Yes      | Foreign Key | References `USER.id` |
| subtotal         | REAL     | Yes      |             | Total before tax     |
| tax_amount       | REAL     | Yes      |             | Calculated tax       |
| shipping_amount  | REAL     | Yes      |             | Shipping cost        |
| total_amount     | REAL     | Yes      |             | Final charged total  |
| status           | TEXT     | Yes      |             | Order status         |
| shipping_address | TEXT     | Yes      |             | Ship-to address      |
| billing_address  | TEXT     | Yes      |             | Billing address      |
| created_at       | DATETIME | Yes      |             | Order creation time  |

# Order_Item
| Field      | SQL Type | Required | Key         | Description             |
| ---------- | -------- | -------- | ----------- | ----------------------- |
| id         | INTEGER  | Yes      | Primary Key | Line ID                 |
| order_id   | INTEGER  | Yes      | Foreign Key | References `ORDER.id`   |
| product_id | INTEGER  | Yes      | Foreign Key | References `PRODUCT.id` |
| quantity   | INTEGER  | Yes      |             | Quantity ordered        |
| unit_price | REAL     | Yes      |             | Price per unit          |
| line_total | REAL     | Yes      |             | Subtotal for this line  |

## Data Examples
# User
| id | email                                                 | first_name | last_name | role     | created_at           |
| -- | ----------------------------------------------------- | ---------- | --------- | -------- | -------------------- |
| 1  | admin@aurum.com        | Admin      | User      | admin    | 2025-09-01T10:00:00Z |
| 2  | collector@example.com| Alex       | Collector | customer | 2025-09-05T14:30:00Z |
| 3  | artlover@example.com   | Jamie      | Rivera    | customer | 2025-09-07T09:15:00Z |

# Category
| id | name       | description                 |
| -- | ---------- | --------------------------- |
| 1  | Artifacts  | Historical objects          |
| 2  | Paintings  | Original and limited prints |
| 3  | Sculptures | 3D art pieces               |

# Product
| id | name                  | price  | category_id | is_active |
| -- | --------------------- | ------ | ----------- | --------- |
| 1  | Ancient Bronze Coin   | 399.99 |  1           | 1         |
| 2  | Renaissance Portrait  | 1299.0 |  2           | 1         |
| 3  | Marble Bust Sculpture | 899.5  |  3           | 1         |
| 4  | Vintage Map of Europe | 249.0  |  1           | 1         |

## Cart
| id | user_id | created_at           | updated_at           |
| -- | ------- | -------------------- | -------------------- |
| 1  | 2       | 2025-09-10T10:00:00Z | 2025-09-10T10:05:00Z |
| 2  | 3       | 2025-09-11T16:20:00Z | 2025-09-11T16:25:00Z |

## Cart_Item
| id | cart_id | product_id |  unit_price_at_add |
| -- | ------- | ---------- |  ----------------- |
| 1  | 1       | 1          |  399.99            |
| 2  | 1       | 4          |  249.00            |
| 3  | 2       | 3          |  899.50            |

## Order
| id | user_id | subtotal | tax_amount | shipping_amount | total_amount | status  | created_at           |
| -- | ------- | -------- | ---------- | --------------- | ------------ | ------- | -------------------- |
| 1  | 2       | 1048.98  | 83.92      | 14.99           | 1147.89      | paid    | 2025-09-12T12:00:00Z |
| 2  | 3       | 899.50   | 71.96      | 19.99           | 991.45       | shipped | 2025-09-14T09:45:00Z |

## Order_Item
| id | order_id | product_id | unit_price | line_total |
| -- | -------- | ---------- | ---------- | ---------- |
| 1  | 1        | 1          | 399.99     | 799.98     |
| 2  | 1        | 4          | 249.00     | 249.00     |
| 3  | 2        | 3          | 899.50     | 899.50     |

## Database Seed Data
# Summary
| Entity     | Seeded?  | Purpose                        |
| ---------- | -------- | ------------------------------ |
| USER       | Yes      | Admin + demo accounts          |
| CATEGORY   | Yes      | Initial category structure     |
| PRODUCT    | Yes      | Initial inventory              |
| CART       | No       | Created at runtime             |
| CART_ITEM  | No       | Created when users add to cart |
| ORDER      | Optional | Demo orders for admin testing  |
| ORDER_ITEM | Optional | Demo line items                |

# User Seed Data
| id | email                                         | role     |
| -- | --------------------------------------------- | -------- |
| 1  | [admin@example.com](mailto:admin@example.com) | admin    |
| 2  | [demo@example.com](mailto:demo@example.com)   | customer |

# Category Seed Data
| id | name       |
| -- | ---------- |
| 1  | Artifacts  |
| 2  | Paintings  |
| 3  | Sculptures |

# Product Seed Data
| id | name                  | price  |  category_id |
| -- | --------------------- | ------ |  ----------- |
| 1  | Ancient Bronze Coin   | 399.99 |  1           |
| 2  | Renaissance Portrait  | 1299.0 |  2           |
| 3  | Marble Bust Sculpture | 899.5  |  3           |

## Authentication and Authorization Plan






