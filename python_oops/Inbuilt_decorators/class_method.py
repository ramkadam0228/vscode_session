class employee:
    company_name='Google'
                  
    @classmethod
    def set_company_name(cls, name):
        cls.company_name=name


class Manager(employee):
    pass

print(employee.company_name)
employee.set_company_name(name="Microsoft")
print(employee.company_name)
print(Manager.company_name)

"""
We can modify class level attributes by using class method..... Overiding the value of class variable using class Method"""