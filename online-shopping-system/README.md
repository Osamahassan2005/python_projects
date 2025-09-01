Report: Online Shopping System 🛍 (CLI & Streamlit-Based Web App)

0. Web App Live (https://online-shopping-system-app.streamlit.app/) 


1. Introduction

The Online Shopping System is a Python-based application designed to facilitate online shopping operations. Initially developed as a Command-Line Interface (CLI) application, it has now been enhanced into a Streamlit-based Web Application for a more user-friendly shopping experience. The system includes functionalities for both Admin and Customers, allowing product management, cart operations, order placement, and now, online payments with receipt generation.


---

2. System Features

CLI-Based Online Shopping System

Admin Features:

1. View Admin Details – Displays admin credentials.


2. Add Products – Allows the admin to add new products.


3. Update Stock – Modifies stock quantity for existing products.


4. Remove Products – Deletes products from the inventory.


5. View Products – Displays all available products.



Customer Features:

1. View Available Products – Displays all items in stock.


2. Add Products to Cart – Customers can add items to their cart.


3. View and Update Cart – Reviews and modifies cart items.


4. Place Order – Confirms order placement.




---

Streamlit-Based Web App Features

Admin Features:

1. Interactive Dashboard – View and manage products visually.


2. Add Products – Add new products through web forms.


3. Update Stock – Modify product quantity dynamically.


4. Remove Products – Delete products using buttons.


5. View Products – Display products in an organized table.



Customer Features:

1. Browse Products – Displays products with images and details.


2. Add to Cart – Select items and quantities via UI.


3. Cart Management – Update or remove items from the cart.


4. Secure Checkout – Users can pay before checkout for convenience.


5. Download Receipt (DOCX) – Customers can download an order summary.




---

3. Sample Execution & Output

CLI Version Sample Execution

Admin Menu:

Admin Options:  
1) View Details  
2) Add Product  
3) Update Stock  
4) Remove Product  
5) View Products  
6) Logout

Example Output (Viewing Products):

Available Products:  
1. Laptop - $1000 (Stock: 5)  
2. Smartphone - $500 (Stock: 10)

Example Output (Adding a Product):

Enter Product name: Headphones  
Enter Product price: 100  
Enter Product stock: 15  

Output: Headphones added successfully!

Customer Menu:

Customer Options:  
1) View Products  
2) Add to Cart  
3) View Cart  
4) Checkout  
5) Exit

Example Output (Adding to Cart):

Enter Product name: Laptop  
Enter Quantity: 1  

Output: Laptop added to cart!

Example Output (Checkout):

Proceed to checkout? (yes/no): yes  

Output: Order placed successfully!


---

Streamlit Web App Sample Execution

Admin Interface

Product Dashboard: Displays a table of all products.

Add Product Form: Admin enters details and clicks "Add Product".

Stock Update: Admin selects a product, enters a new quantity, and updates.


Customer Interface

Browsing Products: Users see a table with product names, prices, and stock.

Adding to Cart: Clicking “Add to Cart” updates the session cart.

Cart View: Displays selected items with an option to modify them.

Checkout: Users can choose to pay before checkout.

Download Receipt: After payment, users can download a DOCX file with order details.


---

5. Conclusion

The Online Shopping System has evolved from a CLI-based application to a modern web application using Streamlit. The web version enhances usability with an interactive UI, online payments, and receipt generation, making the shopping experience smoother and more efficient. This transformation makes the system more user-friendly and accessible, providing a seamless shopping experience. 
