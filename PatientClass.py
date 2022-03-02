 
# PatientClass.py - Write a class named Patient that has the following attributes 
# - ID, name, address, phone, veteran_status (True or False).
#  The Patient class’s __init__ method should accept an argument for each attribute. 
# The Patient class should have accessor methods only for each attribute.


class PatientClass: #create a class named Patient Class so Cahson doesnt yell at me 

    def __init__(self, ID, name, address, phone, veteran_status): # initializer (constructor) of the Patient Class
        self.__ID = ID
        self.__name = name
        self.__address = address
        self.__phone = phone 
        self.__veteran_status = veteran_status
    
    def get_ID(self): # accessor for name attribute
        return self.__ID
    
    def get_name(self): # accessor for name attribute
        return self.__name

    def get_address(self): # accessor for address attribute
        return self.__address 
    
    def get_phone(self): # accessor for phone attribute
        return self.__phone

    def get_veteran_status(self): # accessor for veteran_status attribute
        return self.__veteran_status