# for i in range(10):
#     print(i)

for _ in range(10):
    print("Hello Good Morning")

""" single underscore is place holder for varibale not being used, may be in loop etc"""

# self._protected --> This can be accessible form anywhere
# self.__private --> This is only accessible inside class


# for _ in range(10):
#     print("hello good morning")
 
# """
# _ : we are not using this
# """
# print(_)
 
# def avg(a,b,c):
#     summ=a+b+c
#     average=summ/3
#     return(summ,average)
 
# _,average=avg(10,20,30)
# print(average)
 
 
class Myclass:
    def __init__(self):
        self._protected="Protected" # this we can access anywhere
        self.__private="Private"  # we can access only inside the class
 
    def show(self):
        print(self.__private)
        print(self._protected)
 
#print(Myclass().__private) #error
 
print(Myclass()._Myclass__private)
 
 
""""
observation1: singleunderscore variable anywhere can use
observation-2: double underscore varibale can use only inside class
               youcan not use outside
 
observation-3: if youwant to use double underscore variable
               outside the class we need to take the help of main class
"""
print(Myclass().__private) #error
 
print(Myclass()._Myclass__private) # works