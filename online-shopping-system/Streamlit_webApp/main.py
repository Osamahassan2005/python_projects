# app.py (Streamlit version)
import streamlit as st
import time
from models.product import Product
from users.customer import Customer
from users.admin import Admin
import os

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "main_menu"
# Admin Menu
def admin_menu(admin):
    """Handles Admin operations in Streamlit"""
    st.title(f"Admin Dashboard")
    st.sidebar.title("Admin Options")
    choice = st.sidebar.selectbox(
        "Choose an option:",
        [
            "View Details",
            "Add Product",
            "Update Stock",
            "Remove Product",
            "View Products",
            "Logout",
        ],
        key="admin_menu_selectbox",  # Unique key for this selectbox
    )

    if choice == "View Details":
        admin.show_details()
    elif choice == "Add Product":
        st.subheader("Add Product:")
        st.write('-'*40)
        product_name = st.text_input("Enter Product name:", key="admin_add_product_name").upper()
        price = st.number_input("Enter Product price:", min_value=0, key="admin_add_product_price")
        stock = st.number_input("Enter Product stock:", min_value=0, key="admin_add_product_stock")
        if st.button("Add Product", key="admin_add_product_button"):
            admin.Add_products(product_name, price, stock)
    elif choice == "Update Stock":
        st.subheader("Update Stock:")
        st.write('-'*40)
        product_name = st.selectbox("Enter product name:", key="admin_update_stock_name",options=Product.get_product_names())
        quantity = st.number_input("Enter quantity:", min_value=0, key="admin_update_stock_quantity")
        if st.button("Update Stock", key="admin_update_stock_button"):
            admin.Update_stock(product_name, quantity)
    elif choice == "Remove Product":
        st.subheader("Remove Product:")
        st.write('-'*40)
        product_name = st.selectbox("Enter product name to remove:", key="admin_remove_product_name",options=Product.get_product_names())
        if st.button("Remove Product", key="admin_remove_product_button"):
            admin.remove_product(product_name)
    elif choice == "View Products":
        st.subheader("Available Products:")
        Product.display_products()
    elif choice == "Logout":
        st.session_state.page = "main_menu"  # Return to main menu
        st.session_state.pop("admin", None)  # Clear admin data
        st.success("Logout Successful!")
        time.sleep(2) #wait for 2 seconds
        st.rerun()  # Force rerun to update the UI

# Customer Menu
def customer_menu(customer):
    """Handles Customer operations in Streamlit"""
    st.title("Customer Dashboard")
    st.sidebar.title("Customer Options")
    select = st.sidebar.selectbox(
        "Choose an option:",
        [
            "View available products",
            "Add product to cart",
            "View Cart",
            "Remove product from cart",
            "Payment and Checkout",
            "Back to main menu",
        ],
        key="customer_menu_selectbox",  # Unique key for this selectbox
    )

    if select == "View available products":
        st.subheader("Available Products:")
        Product.display_products()
    elif select == "Add product to cart":
        st.subheader("Add Product to Cart:")
        st.write('-'*40)
        product_name = st.selectbox("Select product to add to cart:", key="customer_add_to_cart_name",options=Product.get_product_names())
        quantity = st.number_input("Enter quantity:", min_value=1, key="customer_add_to_cart_quantity")
        if st.button("Add to Cart", key="customer_add_to_cart_button"):
            customer.add_to_cart(product_name, quantity)
    elif select == "View Cart":
        customer.view_cart()
    elif select == "Remove product from cart":
        st.subheader("Remove Product from Cart:")
        st.write('-'*40)
        product_name = st.selectbox("Select product name to remove:", key="customer_remove_from_cart_name",options=Product.get_product_names())
        if st.button("Remove from Cart", key="customer_remove_from_cart_button"):
            customer.remove_to_cart(product_name)
    elif select == "Payment and Checkout":
        st.subheader("Payment And Checkout:")
        st.write('-'*40)
        customer.checkout()
        customer.generate_receipt()
    elif select == "Back to main menu":
        st.session_state.page = "main_menu"  # Return to main menu
        st.session_state.pop("customer", None)  # Clear customer data
        st.info("Returning to the main menu...")
        time.sleep(2)
        st.rerun()  # Force rerun to update the UI

# Main Menu
def main_menu():
    """Main menu of the Online Shopping System in Streamlit"""
    st.title("Online Shopping System 🛍")
    st.sidebar.title("Main Menu")
    option = st.sidebar.selectbox(
        "📍 Select an option:",
        [   "Home",
            "Register Admin",
            "Admin Login",
            "Customer Login",
            "Exit",
        ],
        key="main_menu_selectbox",  # Unique key for this selectbox
    )
    if option == "Home":
        st.write("Welcome to the Online Shopping System!")
        st.image(os.path.join(os.getcwd(), "Streamlit-App/online-shopping.jpg"))
        st.balloons()
        st.subheader("Instructions :")
        st.write('-'*40)
        st.write("1. Please select an option from the sidebar to continue.")
        st.write('2. You can register as an admin .')
        st.write('3. You can login as an admin or customer.')
        st.write('4. You can exit the program.')
        st.write('5. You can view the products and add them to your cart.')
        st.write('6. You can checkout and view your order history.')
        st.write('-'*40)
       
        st.write("📍**Developed by**: Osama Hassan")
        st.markdown('https://github.com/Osamahassan2005')
        
 
    if option == "Register Admin":
        st.subheader("Register Admin")
        your_name = st.text_input("Enter Your Name:", key="main_register_admin_name").upper()
        your_password = st.text_input("Enter Your Password:", type="password", key="main_register_admin_password")
        if st.button("Register", key="main_register_admin_button") and your_name and your_password:
            new_admin = Admin(your_name, your_password)
            new_admin.save_admin()
        else:
            st.info("Please enter your name and password to register.")
    elif option == "Admin Login":
        st.subheader("Admin Login")
        user_name = st.text_input("Enter Admin name:", key="main_admin_login_name").upper()
        user_password = st.text_input("Enter Admin Password:", type="password", key="main_admin_login_password")
        if st.button("Login", key="main_admin_login_button") and user_name and user_password:
            Admin.login(user_name, user_password)
            st.session_state.admin = Admin(user_name, user_password)
            st.session_state.page = "admin_menu"  # Navigate to admin menu
            st.rerun()  # Force rerun to update the UI
        else:
            st.info("Please enter your name and password to login.")
    elif option == "Customer Login":
        st.subheader("Customer Login:")
        st.write('-'*40)
        customer_name = st.text_input("Enter your name:", key="main_customer_name").upper()
        if st.button("Continue as Customer", key="main_customer_button") and customer_name:
            st.session_state.customer = Customer(customer_name)
            st.session_state.page = "customer_menu"  # Navigate to customer menu
            st.rerun()  # Force rerun to update the UI
        else:
            st.info("Please enter your name to continue.")
    elif option == "Exit":
        st.info("Goodbye! Thank you for using our service.")
        st.stop()

# Main App Logic
def main():
    """Main function to handle navigation"""
    if st.session_state.page == "main_menu":
        main_menu()
    elif st.session_state.page == "admin_menu":
        admin_menu(st.session_state.admin)
    elif st.session_state.page == "customer_menu":
        customer_menu(st.session_state.customer)

# Run the app
if __name__ == "__main__":
    main()
