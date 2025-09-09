""" Nested functions"""

"""
we want to call add function inside multiplication
whenever we want to use a function inside another function
we need to use self
"""
# from python_opps.recap1 import MATH_FUNCTION
class MATH_FUNCTION:
 
    def add(self,a,b):
        print(a+b)
 
    def mul(self,a,b):
        ans3=self.add(a,b)
        print(ans3)
        # self.utils().creat_a_file('dummy1.txt')
        print((a*b))
    
        
MATH_FUNCTION().mul(10,30)
