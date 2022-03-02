# Write a class named Procedure that represents a medical procedure that has been performed on a patient. 
# The Procedure class should have the following attributes - 
# Name of the procedure, Date of the procedure, Name of the practitioner who performed the procedure,
# Charges for the procedure and patient ID.
# The Procedure class’s __init__ method should accept an argument for each attribute.
# The Procedure class should have accessor methods only for each attribute.

class ProcedureClass:

    def __init__(self, name, date, practitioner, charges, patient_ID): # initializer (constructor) of the Patient Class

        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges
        self.__patient_ID = patient_ID

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date
    
    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    def get_patient_ID(self):
        return self.__patient_ID
    

    



