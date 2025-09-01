from models.product import Product
from users.customer import Customer
from users.admin import Admin

def admin_menu(admin):
    """Handles Admin operations"""
    while True:
        print('''\nAdmin Options:
              1) View Details
              2) Add Product
              3) Update Stock
              4) Remove Product
              5) View Products
              6) Logout
        ''')
        choice = input('Enter your choice: ')
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            admin.show_details()
        elif choice == 2:
            product_name = input('Enter Product name: ')
            price = float(input('Enter Product price: '))
            stock = int(input('Enter Product stock: '))
            admin.Add_products(product_name, price, stock)
        elif choice == 3:
            product_name = input('Enter product name: ')
            quantity = int(input('Enter quantity: '))
            admin.Update_stock(product_name, quantity)
        elif choice == 4:
            product_name = input('Enter product name to remove: ')
            admin.remove_product(product_name)
        elif choice == 5:
            Product.display_products()
        elif choice == 6:
            print('Logout Successfully!')
            break
        else:
            print("Invalid choice! Please select 1 - 6.")

def customer_menu(customer):
    """Handles  operations"""
    print('-' * 45)
    print(f'Hello, {customer.name}!')
    print('-' * 45)
    while True:
        print('''\nCustomer Options:
              1) View available products
              2) Add product to cart
              3) View Cart
              4) Remove product to cart
              5) Checkout
              6) View Order History
              7) Back to main menu
        ''')
        select = input('Enter your choice: ')
        if select.isdigit():
            select = int(select)
        else:
            print("Invalid input! Please enter a number.")
            continue

        if select == 1:
            Product.display_products()
        elif select == 2:
            product_name = input('Enter product name to add : ')
            quantity = int(input('Enter quantity: '))
            customer.add_to_cart(product_name, quantity)
        elif select == 3:
            customer.view_cart()
        elif select == 4:
            product_name = input('Enter product name to remove : ')
            customer.remove_to_cart(product_name)
        elif select == 5:
            customer.checkout()
        elif select == 6:
            customer.view_order_history()
        elif select == 7:
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 - 6.")

def main():
    """Main menu of the Online Shopping System"""
    while True:
        print('=' * 45)
        print('Welcome to the Online Shopping System :)')
        print('=' * 45)
        print('''
              1) Register Admin
              2) Admin LogIn
              3) Customer
              4) Exit
        ''')
        option = input("Select an option: ")

        if option.isdigit():
            option = int(option)
        else:
            print("Invalid input! Please enter a number.")
            continue

        if option == 1:
            your_name = input('Enter Your Name: ')
            your_password = input('Enter Your Password: ')
            new_admin = Admin(your_name, your_password)
            new_admin.save_admin()

        elif option == 2:
            user_name = input('Enter Admin name: ')
            user_password = input('Enter Admin Password: ')
            print('-' * 40)
            if Admin.login(user_name, user_password):
                admin = Admin(user_name, user_password)
                print('-' * 40)
                admin_menu(admin)

        elif option == 3:
            customer_name = input('Enter your name: ')
            customer = Customer(customer_name)
            customer_menu(customer)

        elif option == 4:
            print("\nGoodbye! Thank you for using our service.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 - 4.")

main()

# created by @usama_hassan