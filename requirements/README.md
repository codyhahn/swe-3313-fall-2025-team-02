# Requirements
- **Version 1**
  - **T2E-1 - User Accounts and Authentication**
    - **T2S-1** - User Self-Registration
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** The system must allow users to self-register by creating an account with a unique username and password (minimum 6 characters)
     
    - **T2S-2** - User Login
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** The system must allow users to log in with their registered username and password
     
    - **T2S-3** - Admin Login
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** The system must allow administrators to log in using admin credentials
    
    - **T2S-4** - Promote User to Admin
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** An admin must be able to transform a registered user account into an admin account

  - **T2E-2 - Inventory Display and Shopping Cart**
    - **T2S-5** - View Inventory
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** After login, users must see a list of available inventory sorted by highest to lowest price
        
    - **T2S-6** - Inventory Item Details
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** Each inventory item must display a name, at least one picture, price, and short description
        
    - **T2S-7** - Add Items to Cart
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** Users must be able to add multiple items to a shopping cart
        
    - **T2S-8** - Sold Item Restriction
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** The system must prevent users from viewing or purchasing items that are already sold

    - **T2S-9** - Search Inventory
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** Users must be able to search inventory by typing in a search box that matches words against item names and descriptions
        
    - **T2S-10** - Price Display Format
      - **Priority:** Must Have  
      - **Effort:** 0.25 days  
      - **Type:** Non-Functional  
      - **Story:** All inventory item prices must be properly formatted with dollar signs, commas, and decimal points

  - **T2E-3 - Checkout and Payment Process**
    - **T2S-11** - Cart View
      - **Priority:** Must Have  
      - **Effort:** 1.5 days  
      - **Type:** Functional  
      - **Story:** The system must allow users to view items in their cart, showing each item’s name, price, and subtotal cost
        
    - **T2S-12** - Prevent Empty Checkout
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** Users must not be able to click Checkout if their shopping cart is empty
     
    - **T2S-13** - Order Abandonment Handling
      - **Priority:** Must Have  
      - **Effort:** 0.25 days  
      - **Type:** Functional  
      - **Story:** If users abandon an order during confirmation, the system must retain items in their cart for future checkout
    
    - **T2S-14** - Remove Items from Cart
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** The user must be able to remove items from their cart, and if all items are removed, automatically return to the main inventory page
        
    - **T2S-15** - Enter Payment Details
      - **Priority:** Must Have  
      - **Effort:** 2.5 days  
      - **Type:** Functional  
      - **Story:** When the user clicks Pay Now, they must enter shipping address, credit card number, phone number, shipping speed, expiration date, and CVV before confirming
        
    - **T2S-16** - Confirm Order Page
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** The Confirm Order page must display item list, subtotal, tax (6%), and total amount including the overnight($29), 3-day($19), and ground($0) Shipping fees.
        
    - **T2S-17** - Complete Order
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** The user must be able to complete their order, which removes items from inventory and generates a receipt
        
    - **T2S-18** - Receipt Details
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** The receipt must show the last four digits of the credit card, shipping address, item list, subtotal, tax, shipping cost, and total
     
    - **T2S-19** - Form Validation
      - **Priority:** Must Have  
      - **Effort:** 1.5 days  
      - **Type:** Functional  
      - **Story:** All user input forms must include validation for required fields, email format, credit card number format, and expiration dates
     
    - **T2S-20** - Order Confirmation Email
      - **Priority:** Must Have  
      - **Effort:** 1 day  
      - **Type:** Functional  
      - **Story:** The system must display a browser-based receipt that mimics an email confirmation for completed orders

  - **T2E-4 - Admin Tools and Reports**
    - **T2S-21** - Generate Sales Report
      - **Priority:** Must Have  
      - **Effort:** 2.5 days  
      - **Type:** Functional  
      - **Story:** Administrators must be able to generate a sales report showing all purchased items and who purchased them
        
    - **T2S-22** - Sales Report Auto-Update
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** The sales report must update automatically after each completed order
        
    - **T2S-23** - Remove Sold Items from Inventory
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** Purchased items must disappear from the user’s inventory list once sold and appear in the sales report
     
    - **T2S-24** - Method to Add Inventory
      - **Priority:** Must Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** Administrators must have a method to add new inventory items to the system (basic backend method acceptable for V1)
        
  - **T2E-5 - Visual Design and Mockups**
    - **T2S-25** - High-Fidelity Mockups
      - **Priority:** Must Have  
      - **Effort:** 3 days  
      - **Type:** Non-Functional  
      - **Story:** A high-fidelity mockup of all major screens and application flow must be created before coding begins
---
- **Version 2**
  - **T2E-6 - Enhanced User Experience**
    - **T2S-26** - Multiple Item Images
      - **Priority:** Needs to Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** Users should be able to upload and view multiple pictures per inventory item
        
  - **T2E-7 - Advanced Admin Capabilities**
    - **T2S-27** - View Receipt from Sales Report
      - **Priority:** Needs to Have  
      - **Effort:** 2.5 days  
      - **Type:** Functional  
      - **Story:** Administrators should be able to click on a sold item in the sales report to view the related receipt
        
    - **T2S-28** - Export Sales Report
      - **Priority:** Needs to Have  
      - **Effort:** 2 days  
      - **Type:** Functional  
      - **Story:** Administrators should be able to export the sales report to CSV format
        
  - **T2E-8 - Visual Design and Mockups**
    - **T2S-29** - High-Fidelity Mockups
      - **Priority:** Needs to Have  
      - **Effort:** 3 days  
      - **Type:** Non-Functional  
      - **Story:** A high-fidelity mockup of all major screens and application flow must be created before coding begins
        
  - **T2E-9 - UI and Usability Enhancements**
    - **T2S-30** - Enhanced Navigation
      - **Priority:** Wants to Have  
      - **Effort:** 1.5 days  
      - **Type:** Functional  
      - **Story:** The user interface should include enhanced navigation (forward, back, and cancel buttons) for easier browsing
        
    - **T2S-31** - Admin Add Inventory Form
      - **Priority:** Wants to Have  
      - **Effort:** 3 days  
      - **Type:** Functional  
      - **Story:** Administrators should have a web-based form to add new inventory items (with name, description, price, and photo upload)
     
    - **T2S-32** - Bulk Inventory Upload
      - **Priority:** Wants to Have  
      - **Effort:** 3 days  
      - **Type:** Functional  
      - **Story:** Administrators should be able to bulk upload inventory items via CSV file with support for name, description, price, and image URLs
