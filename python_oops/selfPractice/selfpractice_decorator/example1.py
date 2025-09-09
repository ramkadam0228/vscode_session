# Question:
# Define a class named American which has a static method called printNationality.

# Hints:

# Use @staticmethod decorator to define class static method.

class America():

    @staticmethod
    def printNationality():
        print("America")

# anAmerica = America()         # Here Object is created
# anAmerica.printNationality()  # Method is called using object
America.printNationality()      # Method can be called even without creating object as the method is static

# -----------------------------------------------------------------------------------------------------------
# Question:
# Define a class named American and its subclass NewYorker. 
# Hints:
# Use class Subclass(ParentClass) to define a subclass.


class India():
    def inIndia():
        print("I am in India class")

class Mumbai(India):
    def nawMumbai():
        print("I am in New Mumbai")

Mumbai.inIndia()
Mumbai.nawMumbai()