import csv
import os

class Product:
    '''Product class for managing products'''
    def __init__(self,product_name,price,stock):
        self.product_name=product_name
        self.price = price
        self.stock =stock
    def save_products(self):
        '''Save product details to products.csv'''
        file_exists=os.path.isfile('products.csv')
        products=[]
        if file_exists:
            with open('data/products.csv','r') as f:
               reader=csv.reader(f)
               products=[row for row in reader if row]
        for row in products:
              if len(row)>0 and  row[0].lower() == self.product_name.lower():   
                 print(f'Product {self.product_name} , already exists .Not adding again.')
                 return
        with open('data/products.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow([self.product_name,self.price,self.stock])
        print(f'product {self.product_name} , added Succesfully.')
    #static method is used to access the method without creating an instance of the class
    @staticmethod
    def display_products():
        '''Display available products'''
        try:
            with open('data/products.csv') as f:
                reader=csv.reader(f)
                products=[row for row in reader if row]
                if not products:
                   print('No products available.')
                   return
                print('\n Available Products:')
                print('-'*30)
                for index,row in enumerate(products,start=1):
                    print(f'{index}) {row[0]} - ${row[1]} (stock:{row[2]})')
                print('-'*30)
        except FileNotFoundError :
                print('No product file found.')
    @staticmethod
    def update_stock(product_name,quantity):
        '''Update stock of existing product'''
        try:
            quantity=int(quantity)
            with open('data/products.csv') as f:
                reader=csv.reader(f)
                products=[row for row in reader if row]
                product_found=False
            for row in products:
                if row[0].lower() == product_name.lower():
                    current_stock=int(row[2].strip())
                    if current_stock >= quantity:
                        row[2]=str(current_stock-quantity)
                        product_found=True
                    else:
                        print('Not enough stock available.')
            if product_found:
                with open('data/products.csv','w',newline='') as f:
                    writer=csv.writer(f)
                    writer.writerows(products)
                    print('Stock Updated.')
            else:
                print('Product not found.')
        except FileNotFoundError :
                print('No product file found.')


# c=Product('Laptop',900,10)
# c2=Product('Mobile',600,10)
# c.save_products()
# c2.save_products()
# Product.display_products()

        


