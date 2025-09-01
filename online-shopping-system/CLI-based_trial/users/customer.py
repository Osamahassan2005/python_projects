from users.user import User
from models.product import Product
from models.cart import ShoppingCart
from datetime import datetime
import csv
# customer class inherit from user class
class Customer(User):
    '''Customer class for shopping'''
    def __init__(self,name):
        '''Initialize customer with name and role'''
        super().__init__(name,role='Customer')
        self.cart=ShoppingCart()
    def add_to_cart(self,product_name,Quantity):
        '''Add product to cart'''
        try:
           with open('data/products.csv','r') as f:
                  reader=csv.reader(f)
                  products=[row for row in reader if row]
        except FileNotFoundError:
           print('File Not Found')
           return
        products_found=False
        for row in products:
            if row[0].lower()==product_name.lower():
                products_found=True
                price=float(row[1])
                stock=int(row[2])
                if stock >= Quantity :
                    self.cart.add_product(product_name,price,Quantity)
                    print(f'{Quantity} x {product_name} added to cart at ${price} each!')
                else:
                    print(f'Not enough stock for "{product_name}", Available stock: {stock}.')
                return
        if not products_found:
            print(f'Product "{product_name}" not found .')
    def remove_to_cart(self,product_name):
        '''Remove product from cart'''
        self.cart - product_name
    def view_cart(self):
        '''View cart'''
        if not self.cart.items:
            print('Your cart is empty.')
            return
        total_price=self.cart.get_total_price()
        time=datetime.now().strftime("%y-%m-%d %H:%M:%S")
        reciept=[]
        reciept.append(f"\n{self.name.upper()}'s CART")
        reciept.append("="*30)
        reciept.append(f"Date & Time: {time}")
        reciept.append(f"Customer: {self.name}")
        reciept.append("-"*30)
        for product,details in self.cart.items.items():
            reciept.append(f"{product} x{details['Quantity']} - ${details['Price']} each")
        reciept.append("-"*30)
        reciept.append(f"Total amount: ${total_price}")
        reciept.append("="*30)
        print('\n'.join(reciept))
    def save_order_history(self):
        '''Save order history'''
        with open("data/order_history.csv","a",newline="") as f:
            writer=csv.writer(f)
            for product,details in self.cart.items.items():
                writer.writerow([self.name,product,details['Quantity'],details['Price']])
    def view_order_history(self):
        '''View order history'''
        try:
            with open('data/order_history.csv','r') as f:
                 reader=csv.reader(f)
                 orders=list(reader)
            if not orders :
                print('\n No order history found.')
                return
            print('-'*45)
            print(f"{self.name}'s Order History")
            print('-'*45)
            found=False
            for order in orders:
                if order[0] == self.name:
                    found=True
                    print(f"{order[1]} - {order[2]} pcs - ${order[3]}each")
                    print('-'*45)
            if not found :
                print(f'No history availabe for {self.name} name.')
        except FileNotFoundError:
            print('No order history found')
    def checkout(self):
        '''Checkout'''
        if not self.cart.items:
            print('Your cart is empty.')
        total_price=self.cart.get_total_price()
        time=datetime.now().strftime("%y-%m-%d %H:%M:%S")
        #create reciept
        reciept=[]
        reciept.append("\nRECIEPT")
        reciept.append("="*30)
        reciept.append(f"Date & Time: {time}")
        reciept.append(f"Customer: {self.name}")
        reciept.append("-"*30)
        for product,details in self.cart.items.items():
            reciept.append(f"{product} x{details['Quantity']} - ${details['Price']} each")
        reciept.append("-"*30)
        reciept.append(f"Total amount: ${total_price}")
        reciept.append("="*30)
        reciept.append("\nThank you for shopping with us!")
        #dispaly reciept
        print('\n'.join(reciept))
        #update stock
        for product_name,details in self.cart.items.items():
            quantity=int(details['Quantity'])
            Product.update_stock(product_name,quantity)
        self.save_order_history()
        self.cart.clear_cart()

