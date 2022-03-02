# Classes are essentially templates, like a cookie cutter. We can make many like objects (cookies) by using a cookie cutter
# - Classes are really useful for making many like things.
# - An instance of a class, is an object made using the class template
# - Object and instance are essentially synonymous, you could say, 
#   Tommy is an Object of the person class, or Tommy is an instance of the person class
# - Attributes are class variabiles
# - Methods are class functions

# A.) Class structure (The cookie cutter template, not actually an object of the class)
class Car: # Class definition header, the class name goes here
    def __init__(self, make, color, price): # Class init function (this gets called secretley when you make an object with the class)
        self.__make = make # Attribute
        self.__color = color # Attribute
        self.__price = price
    
    def get_make(self): # Get method
        return self.__make
    def get_color(self): # Get method
        return self.__color
    def get_price(self):
        return self.__price
    def set_make(self, make): # Set method
        self.__make = make
    def set_color(self, color): # Set method
        self.__color = color
    def set_price(self, price): # Set method
        self.__price = price

    def discount(self):
        return self.__price * 0.05
    def sales_tax(self):
        return self.__price * 0.10


#   A1.) MAKE an instance/object of the class
mycar = Car('BMW','Silver', 10000) # This is what uses the init function to make a new object of the class, it takes the same parameters that the __init__ function takes
#   A2.) USE FUNCTIONS of the Car object
print('Base Price:', mycar.get_price(), 'Discount:', mycar.discount(), 'Sales Tax:', mycar.sales_tax())     
#   A3.) CHANGE OBJECT ATTRIBUTES
print('Color before change', mycar.get_color())
mycar.set_color('red')
print('Color after change', mycar.get_color())

print();print() # Ignore this


# B.) Classes in python and what they are
#   B1.) Classes in python are the template we use to make like objects. The objects made using the class are technically of the classe names type
class Person:
    def __init__(self):
        pass

x = Person() # Make instance of class
print(type(x)) # x is a Person object so This prints <class Person>

#   B2.) Class objects alone are simply data stored in memory, if you print a class object it will simply tell you its type and where in memory it is stored
print(x)