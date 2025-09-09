""" Encapsulation is used to process the attributes in a single class itself & restrict direct access to other class

1. Public Members - Public to all, can be access outside class
2. Protected members - Attributes/method using single underscore, semi private
3. Private member -  Attributes/method using Double underscore  
making them inaccesible outside the class        

"""

class employee():
    def __init__(self,name, salary) -> None:
        self.name=name
        # self._salary=salary
        self.__salary=salary

    def display_name(self):
        print(f" Employee Name: {self.name}")

    def get_salary(self):
        print(f"Employee Salary {self.__salary}")

    def set_salary(self, new_salary):
        if new_salary>0:
            self.__salary=new_salary
            print(f"Employee Salary {self.__salary}")
        else:
            print("provide correct value")    

emp=employee("Ram",0)
emp.display_name()
emp.get_salary()
emp.set_salary(15000)
# print("salary:",emp._salary)
print(emp._employee__salary) #--> Works

""" Whenever you want to use private variable outside class object name, class name and variable name"""