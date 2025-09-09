# Question 25
# Level 1

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later

class calc():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    # def add( x, y):
        # print(x+y)
    
    def add(self):
        print(self.a+self.b)


obj = calc(6,7)
obj.add()

  
