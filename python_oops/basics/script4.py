"""
In real time we will write many python file
diiferent developers will cretae differen tasks
but all python tasks collborate at one place main.py
tomorrow the user can change only scripts , then automaticall main file will be affected
from <python file> import <class name>
"""
 
# import script2
from script2 import MATH_FUNCTION
# obj=MATH_FUNCTION()
# print(dir(obj))  # how many methods this class has
# # this class has 4 methods add, sub, mul and div
# print(help(MATH_FUNCTION().add))

if __name__ == "__main__":
    obj4=MATH_FUNCTION()
    obj4.add(1000,2000)
    obj4.mul(50,50)
    obj4.sub(1000,200)
    obj4.div(1000,200)
 
# obj4=MATH_FUNCTION()
# obj4.add(1000,2000)
# obj4.mul(50,50)
# obj4.sub(1000,200)
# obj4.div(1000,200)
 