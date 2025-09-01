# user class is a parent class for admin and customer class
class User:
    '''User class for user details'''
    def __init__(self,name,role):
        self.role=role
        self.name=name
    def show_details(self):
        '''Show user details'''
        print(f'User Name :{self.name}')
        print(f'User Role :{self.role}')