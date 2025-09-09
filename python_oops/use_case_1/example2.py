"""
if we identify any comman variables inside the class function
we can declare those variables as global by using __init__
step-1: provide the comman variable under init
step-2: remove th comman variables from methods
step-3: access the variables using self
step-4: while you are calling the methods using class
        provide th variables inside the class
"""
class MATH_FUNCTION:
    def __init__(self,a,b):
        self.a=a
        self.b=b
 
    def add(self, e):
        return(self.a+self.b + e)
 
    def mul(self):
        return(self.a*self.b)
   
    def div(self):
        return(self.a/self.b)
 
    def sub(self,c,d):
        # return(self.a-self.b)
        return(c-d)
 
 
 
if __name__=="__main__":
    ans1=MATH_FUNCTION(10,20).add(40)
    ans2=MATH_FUNCTION(30,40).mul()
    ans3=MATH_FUNCTION(10,20).div()
    ans4=MATH_FUNCTION(100,12).sub(40,30)
    print("Addition:",ans1)
    print("multiplication:",ans2)
    print("Division:",ans3)
    print("Subtraction:",ans4)
 