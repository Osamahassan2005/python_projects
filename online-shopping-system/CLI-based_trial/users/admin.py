from users.user import User
import csv
# admin class inherit from user class
class Admin(User):
    ''' Admin class for managing products'''
    def __init__(self, name,password):
        super().__init__(name, role='Admin')
        self.password=password
    def save_admin(self):
        '''Save admin details to admins.csv'''
        try:
            with open('data/admins.csv','r') as f:
                reader=csv.reader(f)
                admins=[row for row in reader if row]
        except FileNotFoundError:
            admins=[]
        for row in admins:
            if row[0].lower()== self.name.lower():
                print(f'Admin "{self.name}" Already exists.')
                return
        with open('data/admins.csv','a',newline="") as f:
            writer=csv.writer(f)
            writer.writerow([self.name,self.password])
        print(f'Admin "{self.name}" added succesfully.')

    #static method is used to access the method without creating an instance of the class
    @staticmethod
    def login(user_name,user_password):
        '''Login admin with name and password'''
        try:
            with open('data/admins.csv','r') as f:
                reader=csv.reader(f)
                for row in reader:
                    if row[0].lower() == user_name.lower() and row[1] == user_password:
                        print(f'Login succesfull, Welcome! "{user_name.upper()}".')
                        return True
        except FileNotFoundError:
            print('Admin File Not Found .')
        print('Incorrect name or password ,please Try again.')
        return False
    def show_details(self):
        print('-'*40)
        super().show_details()
        print(f'Password :{self.password}')
        print(f'Privileges: Can Add, Update, Remove products.')
        print('-'*40)
    def Add_products(self,product_name,price,stock):
        '''Add new product to products.csv'''
        try:
           with open('data/products.csv') as f:
                  lines=f.readlines()
        except FileNotFoundError:
           lines=[]
        product_entry=f'{product_name},{price},{stock}\n'
        if product_entry in lines:
           print(f'Product "{product_name}",already exists .Not adding again.')
           return
        with open('data/products.csv','a') as f:
            f.write(product_entry) 
        print(f'product "{product_name}" added Succesfully.')
    def Update_stock(self,product_name,new_quantity):
        '''Update stock of existing product'''
        try:
           with open('data/products.csv') as f:
                  reader=csv.reader(f)
                  product=list(reader)
        except FileNotFoundError:
           print('File Not Found')
           return
        updated =False
        for row in product:
            if row[0] == product_name:
               row[2]=str(int(row[2])+int(new_quantity))
               updated=True
        if updated:
            with open('data/products.csv','w',newline='') as f:
                 writer=csv.writer(f)
                 writer.writerows(product)
            print(f'Stock Updated Succesfully for product "{product_name}".')
        else:
            print(f'Product "{product_name}" not found.')
    def remove_product(self,product_name):
        '''Remove product from products.csv'''
        try:
           with open('data/products.csv') as f:
                  reader=csv.reader(f)
                  products=list(reader)
        except FileNotFoundError:
           print('File Not Found')
           return
        removed=False
        updated_products=[]
        for row in products:
            if row[0].lower() == product_name.lower() :
               removed=True
            else:
                updated_products.append(row)
        if removed:
            with open('data/products.csv','w',newline='') as f:
                 writer=csv.writer(f)
                 writer.writerows(updated_products)
            print(f'Product "{product_name}" removed succesfully.')
        else:
            print(f'Product "{product_name}" not found.')
