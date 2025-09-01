import csv
import os
import streamlit as st
import pandas as pd

class Product:
    '''Product class for managing products'''
    def __init__(self,product_name,price,stock):
        self.product_name=product_name
        self.price = price
        self.stock =stock
    def add_products(self):
        '''Save product details to products.csv'''
        file_path='Streamlit-App/data/products.csv'
        file_exists=os.path.isfile(file_path)
        products=[]
        if file_exists:
            with open(file_path,'r') as f:
               reader=csv.DictReader(f)
               products=[row for row in reader if row]
            for row in products:
              if len(row)>0 and  row['product_name'].lower() == self.product_name.lower():   
                 st.error(f'Product "{self.product_name}" , already exists .Not adding again.')
                 return
        with open(file_path,'a',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=['product_name','price','stock'])
            if not file_exists or os.stat(file_path).st_size==0:
                writer.writeheader()
            writer.writerow({'product_name':self.product_name,'price':self.price,'stock':self.stock})
        st.success(f'Product "{self.product_name}" , added Succesfully.')
    #static method is used to access the method without creating an instance of the class
    @staticmethod
    def display_products():
        '''Display available products'''
        try:
            df=pd.read_csv('Streamlit-App/data/products.csv')
            if df.empty:
                st.error('No products available.')
                return
            st.write('Available Products:')
            st.table(df)
        except FileNotFoundError:
            st.error('No product file found.')
    @staticmethod
    def update_stock(product_name,quantity):
        '''Update stock of existing product'''
        try:
            quantity=int(quantity)
            file_path='Streamlit-App/data/products.csv'
            with open(file_path,'r') as f:
                reader=csv.DictReader(f)
                products=[row for row in reader if row]
            product_found=False
            for row in products:
                if row['product_name'].strip().lower() == product_name.strip().lower():
                    current_stock=int(row['stock'].strip())
                    if current_stock >= quantity:
                        row['stock']=str(current_stock-quantity)
                        product_found=True
                    else:
                        st.error(f'Not enough stock available for {product_name}.')
            if product_found:
                with open(file_path,'w',newline='') as f:
                    writer=csv.DictWriter(f,fieldnames=['product_name','price','stock'])
                    writer.writeheader()
                    writer.writerows(products)
                for i in range(0):
                    st.success('Stock Updated.')
            else:
                st.error('Product not found for stock update.')
        except FileNotFoundError :
                st.error('No product file found .')
    @staticmethod
    def get_product_names():
        '''Get product names'''
        try:
            with open('Streamlit-App/data/products.csv','r') as f:
                reader=csv.DictReader(f)
                products=[row['product_name'].strip() for row in reader if row]
            return products
        except FileNotFoundError:
            st.error('No product file found.')
