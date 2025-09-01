# shopping cart aggregate to customer class
import streamlit as st
class ShoppingCart:
    '''Shopping cart class for adding and removing products'''
    def __init__(self):
        '''Initialize shopping cart'''
        self.items = {}

    def add_product(self, product_name, price, quantity):
        '''Add product to cart'''
        if product_name in self.items:
            self.items[product_name]['Quantity'] += quantity
        else:
            self.items[product_name] = {'Price': price, 'Quantity': quantity}
    def __sub__(self,product_name):
        '''operator overloading for removing product from cart'''
        if product_name in self.items:
            del self.items[product_name]
            st.success(f'"{product_name}" removed from the cart.')
        else:
            st.error(f'{product_name} is not in the cart')
    def get_total_price(self):
        '''Calculate total cart price'''
        return sum(details['Price'] * details['Quantity'] for details in self.items.values())

    def clear_cart(self):
        '''Clear the cart after checkout'''
        self.items.clear()
        
