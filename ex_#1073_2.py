class User(): 
    """The easiest user mode.""" 
    def __init__(self, first_name, last_name): #it is a method
        """Attributes inizialization: shop_name і store_type."""
        self.first_name = first_name #it is an attribute
        self.last_name = last_name #it is an attribute
        self.login_attempts = 0


    def describe_user(self):
        print(self.first_name,self.last_name)


    def greeting_user(self):
        print(f'Hello, {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0 

class Admin(User):#it is a class              
    def __init__(self, first_name, last_name):#it is a method
        super().__init__(first_name, last_name)
        self.priveleges = ['Allowed to add message','Allowed to delete users',
                          'Allowed to ban users']
    def show_priveleges(self):
        print(self.priveleges)
"""
class Priveleges():
    def __init__(self, first_name, last_name):#it is a method
        super().__init__(first_name, last_name)
        \"""Attributes inizialization: privileges.\"""
        self.priveleges = ['Allowed to add message','Allowed to delete users',
                           'Allowed to ban users']
    def show_priveleges(self):
        print(self.priveleges)
"""
"""Task c & d are not completed."""
