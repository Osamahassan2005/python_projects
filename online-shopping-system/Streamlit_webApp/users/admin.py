from users.user import User
from models.product import Product
import csv
import streamlit as st
import pandas as pd
import os


# admin class inherit from user class
class Admin(User):
    ''' Admin class for managing products'''
    def __init__(self, name,password):
        super().__init__(name, role='Admin')
        self.password=password
    def save_admin(self):
        '''Save admin details to admins.csv'''
        try:
            file_path='Streamlit-App/data/admins.csv'
            file_exists=os.path.isfile(file_path)
            
            with open(file_path,'r') as f:
                reader=csv.DictReader(f)
                admins=[row for row in reader if row]
        except FileNotFoundError:
            admins=[]
        for row in admins:
            if row['Name'].lower()== self.name.lower():
                st.error(f'Admin "{self.name}" Already exists.')
                return
        with open(file_path,'a',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=['Name','Password'])
            if not file_exists or os.stat(file_path).st_size==0:
                writer.writeheader()
            writer.writerow({'Name':self.name,'Password':self.password})
        st.success(f'Admin "{self.name}" added succesfully.')

    #static method is used to access the method without creating an instance of the class
    @staticmethod
    def login(user_name,user_password):
        '''Login admin with name and password'''
        try:
            with open('Streamlit-App/data/admins.csv','r') as f:
                reader=csv.DictReader(f)
                for row in reader:
                    if row['Name'].lower() == user_name.lower() and row['Password'] == user_password:
                        return True
        except FileNotFoundError:
            st.error('Admin File Not Found .')
        st.error('Incorrect name or password ,please Try again.')
        return False
    def show_details(self):
        st.subheader('**Admin Details:**')
        df=[]
        df.append([self.role,self.name,self.password])
        df=pd.DataFrame(df,columns=['Role','Name','Password'])
        st.table(df)
    def Add_products(self,product_name,price,stock):
        product=Product(product_name,price,stock)
        product.add_products()
    def Update_stock(self,product_name,new_quantity):
        '''Update stock of existing product'''
        try:
           file_path='Streamlit-App/data/products.csv'
           file_exists=os.path.isfile(file_path)
           with open(file_path,'r') as f:
                  reader=csv.DictReader(f)
                  product=list(reader)
        except FileNotFoundError:
           st.error('File Not Found')
           return
        updated =False
        for row in product:
            if row['product_name'].strip().lower() == product_name.strip().lower():
               row['stock']=str(int(row['stock'])+int(new_quantity))
               updated=True
        if updated:
            with open(file_path,'w',newline='') as f:
                 writer=csv.DictWriter(f,fieldnames=['product_name','price','stock'])
                 if not file_exists or os.stat(file_path).st_size==0:
                    writer.writeheader()
                 writer.writerows(product)
            st.success(f'Stock Updated Succesfully for product "{product_name}".')
        else:
            st.error(f'Product "{product_name}" not found.')
    def remove_product(self,product_name):
        '''Remove product from products.csv'''
        try:
           file_path='Streamlit-App/data/products.csv'
           file_exists=os.path.isfile(file_path)
           with open(file_path,'r') as f:
                  reader=csv.DictReader(f)
                  products=list(reader)
        except FileNotFoundError:
           st.error('File Not Found')
           return
        removed=False
        updated_products=[]
        for row in products:
            if row['product_name'].strip().lower() == product_name.strip().lower() :
               removed=True
            else:
                updated_products.append(row)
        if removed:
            with open(file_path,'w',newline='') as f:
                 writer=csv.DictWriter(f,fieldnames=['product_name','price','stock'])
                 if not file_exists or os.stat(file_path).st_size==0:
                    writer.writeheader()   
                 writer.writerows(updated_products)
            st.success(f'Product "{product_name}" removed succesfully!')
        else:
            st.error(f'Product "{product_name}" not found.')
