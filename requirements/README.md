# Requirements (This is all subject to change depending on further review)

- Version 1 

  - T2E-1: User Account Management

    - **T2S-1: _Register a new user_**
      - **Priority:** Must Have
      - **Effort:** 1 day
      - **Type:** Functional
      - The user must be able to self-register by creating an account with a unique username and a password that is at least 6 characters long. Admins cannot self-register.

    - **T2S-2: _Log in as a registered user_**
      - **Priority:** Must Have
      - **Effort:** 0.5 day
      - **Type:** Functional
      - The user must be able to log in using their registered credentials. Login must validate credentials and direct the user to the main inventory screen upon success.

  - T2E-2: Inventory Browsing & Cart

    - **T2S-3: _View available inventory_**
      - **Priority:** Must Have
      - **Effort:** 2 days
      - **Type:** Functional
      - After logging in, the user must see a list of all available inventory items sorted by highest to lowest price. Each item must include a short name, picture, price, and brief description. Users cannot see items already sold.

    - **T2S-4: _Search inventory items_**
      - **Priority:** Must Have
      - **Effort:** 1 day
      - **Type:** Functional
      - The user must be able to search the inventory by typing into a search box. The system must match entered words to an item’s name or description and display matching results.

    - **T2S-5: _Add items to shopping cart & manage cart_**
      - **Priority:** Must Have
      - **Effort:** 2 days
      - **Type:** Functional
      - The user must be able to add items to a shopping cart, view the cart, remove items, and adjust quantities. The cart must display a subtotal in USD (formatted with a $ sign and two decimal places).

  - T2E-3: Checkout & Orders

    - **T2S-6: _Checkout flow (start payment)_**
      - **Priority:** Must Have
      - **Effort:** 2 days
      - **Type:** Functional
      - The user cannot click Checkout if the shopping cart is empty. After clicking Checkout, the user must see the list of items in the cart and a subtotal in USD. The user may remove items from this list and return to shopping.

    - **T2S-7: _Payment screen and confirm order_**
      - **Priority:** Must Have
      - **Effort:** 1 day
      - **Type:** Functional
      - From the Checkout page, the user must click Pay Now to start payment. The user must enter a shipping address, credit card number, phone number, and shipping speed. All fields are required. The credit card entry must include card expiration month/year and CVV.

    - **T2S-8: _Complete order, receipt & email_**
      - **Priority:** Must Have
      - **Effort:** 1 day
      - **Type:** Functional
      - After clicking Complete Order, the system must display a receipt that includes the items purchased, subtotal, tax (6%), shipping cost, grand total, shipping address, and the last four digits of the purchaser’s credit card. The receipt must also be automatically emailed to the user (email may be simulated in Version 1).

    - **T2S-9: _Post-purchase behavior_**
      - **Priority:** Must Have
      - **Effort:** 0.5 day
      - **Type:** Functional
      - Once an order completes, purchased items must be removed from the main inventory and must not appear in search results. The sale must be recorded to the sales report. The user may click OK on the receipt to return to the main page; at that point, the cart must be empty.

  - T2E-4: Administrator Management

    - **T2S-10: _Run sales reports_**
      - **Priority:** Must Have
      - **Effort:** 1 day
      - **Type:** Functional
      - Administrators must be able to run a sales report showing all purchases, including item name, buyer username, date, and total amount. Clicking on a sold item must open its corresponding receipt.

    - **T2S-11: _Export sales report to CSV_**
      - **Priority:** Must Have
      - **Effort:** 0.5 day
      - **Type:** Functional
      - Administrators must be able to export sales report data to a CSV file for analysis in Excel or other external tools.

    - **T2S-12: _Add new inventory items_**
      - **Priority:** Must Have
      - **Effort:** 2 days
      - **Type:** Functional
      - Administrators must be able to add inventory items by filling out a form (or database entry) with name, description, price, and picture. If a form is too difficult, a manual method (like entering into a database file) is acceptable. Initially, the store will be empty until inventory is added.

- Version 2

  - T2E-5: Administrator Enhancements

    - **T2S-13: _Edit or delete inventory items_**
      - **Priority:** Wants to Have
      - **Effort:** 1.5 days
      - **Type:** Functional
      - Administrators should be able to edit or delete existing inventory items. Deletions must require confirmation. Edits should update the database immediately.

    - **T2S-14: _View inventory statistics dashboard_**
      - **Priority:** Wants to Have
      - **Effort:** 1 day
      - **Type:** Non-Functional
      - The system should display a simple dashboard showing total sales per day, most popular items, and inventory levels.

  - T2E-6: User Experience Enhancements

    - **T2S-15: _Multiple pictures per item_**
      - **Priority:** Wants to Have
      - **Effort:** 1 day
      - **Type:** Functional
      - The system should allow multiple pictures per item (thumbnail + gallery). This feature can be implemented later if time allows.

    - **T2S-16: _Advanced search filters_**
      - **Priority:** Wants to Have
      - **Effort:** 1 day
      - **Type:** Functional
      - Add optional filters such as price range and item category to refine search results.

---

## Notes

- All prices must be displayed in USD with a dollar sign and two decimal places (e.g., `$10,000.00`).
- Email delivery may be simulated in Version 1.
- Security: all input fields must be validated; sensitive data (credit card numbers) must only store the last four digits for receipts.
- Monetary values should be stored as decimal/currency (base-10, not floating-point).
