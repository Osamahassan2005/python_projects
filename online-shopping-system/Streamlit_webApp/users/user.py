# user class is a parent class for admin and customer class
import streamlit as st
class User:
    '''User class for user details'''
    def __init__(self,name,role):
        self.role=role
        self.name=name
    def show_details(self):
        '''Show user details'''
        st.write(f'**User Name** : {self.name}')
        st.write(f'**User Role** : {self.role}')