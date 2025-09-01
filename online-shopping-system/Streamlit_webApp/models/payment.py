import streamlit as st
class Payment:
    def __init__(self, amount, customer_name):
        self.amount = amount
        self.customer_name = customer_name
        self.payment_method = None
        self.details = []

    def process_payment(self):
        payment_method = st.selectbox('Select payment method', ['Credit/Debit Card', 'Bank Transfer', 'Mobile Money'])
        if payment_method == 'Credit/Debit Card':
            self.payment_method = 'Credit/Debit Card'
            return self.credit_debit_card_payment()
        elif payment_method == 'Bank Transfer':
            self.payment_method = 'Bank Transfer'
            return self.bank_transfer()
        elif payment_method == 'Mobile Money':
            self.payment_method = 'Mobile Money'
            return self.mobile_money()
        st.error('Invalid payment method')
        return False

    def credit_debit_card_payment(self):
        st.write('Please enter your credit/debit card details')
        card_number = st.text_input('Enter your credit/debit card number: ')
        card_expiry = st.text_input('Enter your credit/debit card expiry date (MM/YY): ')
        card_cvv = st.text_input('Enter your credit/debit card CVV: ')
        if st.button('Confirm Payment'):
            if card_number and card_expiry and card_cvv:
                self.details.append(f'Credit/Debit Card: {card_number}, Expiry: {card_expiry}, CVV: {card_cvv}')
                st.success('Payment successful!')
                return True
            st.error('Payment failed! Please fill in all fields.')
        return False

    def bank_transfer(self):
        st.write('Please enter your bank transfer details')
        bank_account_number = st.text_input('Enter your bank account number: ')
        bank_routing_number = st.text_input('Enter your bank routing number: ')
        if st.button('Confirm Payment'):
            if bank_account_number and bank_routing_number:
                self.details.append(f'Bank Transfer: {bank_account_number}, Routing: {bank_routing_number}')
                st.success('Payment successful!')
                return True
            st.error('Payment failed! Please fill in all fields.')
        return False

    def mobile_money(self):
        st.write('Please enter your mobile money details')    
        mobile_money_number = st.text_input('Enter your mobile money number: ')
        mobile_money_provider = st.text_input('Enter your mobile money provider: ')
        if st.button('Confirm Payment'):
            if mobile_money_number and mobile_money_provider:
                self.details.append(f'Mobile Money: {mobile_money_number}, Provider: {mobile_money_provider}')
                st.success('Payment successful!')
                return True
            st.error('Payment failed! Please fill in all fields.')
        return False



# ## cli
# class Payment:
#     def __init__(self, amount,customer_name):
#         self.amount = amount
#         self.customer_name = customer_name
    
#     def process_payment(self):
#         print('''/n which payment method would you like to use?
#         1. Credit/Debit Card
#         2. Bank Transfer
#         3. Mobile Money
#         ''')
#         payment_method = input('Enter the number of the payment method you would like to use: ')
#         if payment_method == '1':
#             self.credit_debit_card_payment()
#         elif payment_method == '2':
#             self.bank_transfer()
#         elif payment_method == '3':
#             self.mobile_money()
#         else:
#             print('Invalid payment method')
            
#     def credit_debit_card_payment(self):
#         print('''/n please enter your credit/debit card details
#         ''')
#         card_number = input('Enter your credit/debit card number: ')
#         card_expiry = input('Enter your credit/debit card expiry date: ')
#         card_cvv = input('Enter your credit/debit card CVV: ')
        
#         print(f'Processing credit card payment of {self.amount} for {self.customer_name}')
#         print(f'Credit/Debit card number: {card_number}')
#         print(f'Credit/Debit card expiry: {card_expiry}')
#         print(f'Credit/Debit card CVV: {card_cvv}')

#     def bank_transfer(self):
#         print('''/n please enter your bank transfer details
#         ''')
#         bank_account_number = input('Enter your bank account number: ')
#         bank_routing_number = input('Enter your bank routing number: ')
        
#         print(f'Processing bank transfer of {self.amount} for {self.customer_name}')
#         print(f'Bank account number: {bank_account_number}')
#         print(f'Bank routing number: {bank_routing_number}')
        
#     def mobile_money(self):
#         print('''/n please enter your mobile money details
#         ''')    
#         mobile_money_number = input('Enter your mobile money number: ')
#         mobile_money_provider = input('Enter your mobile money provider: ')
        
#         print(f'Processing mobile money payment of {self.amount} for {self.customer_name}')
#         print(f'Mobile money number: {mobile_money_number}')
#         print(f'Mobile money provider: {mobile_money_provider}')        
