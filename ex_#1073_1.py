class Shop(): 
    """The easiest shop mode.""" 
    def __init__(self, shop_name, store_type): #it is a method
        """Attributes inizialization: shop_name і store_type."""
        self.shop_name = shop_name #it is an attribute
        self.store_type = store_type #it is an attribute
        self.number_of_units = 0#it is an attribute with value by default
    
    def describe_shop(self):#it is a method
        print(f'Shop name: {self.shop_name}')
        print(f'Store type: {self.store_type}')
         
    
    def open_shop(self):#it is a method
        print("The shop is open!")

    def read_number_of_units(self): #it is a method
        print("This shop has " + str(self.number_of_units) + " units in it.")  
    

    def set_number_of_units(self, num):#it is a method
        self.number_of_units = num

    def increment_number_of_units(self,num):#it is a method
        self.number_of_units += num

class Discout(Shop):#it is a class              
    def __init__(self, shop_name, store_type):#it is a method
        super().__init__(shop_name, store_type)
        self.discount_products = []   
    
    def get_discount_products(self):
        print(str(self.discount_products))
        
#script for the task execution is located in ex_#1073_1.txt
