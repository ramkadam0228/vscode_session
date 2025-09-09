from decorator3_variables import my_decorator
from example3_variables import decorator2

@my_decorator
def add(a,b):
    print(a+b)

@decorator2("Performaing Addition")
def addition(a,b):
    print(a+b)

# @my_decorator
# def add(a,b,c):
#     print(a+b+c)

@my_decorator
def sub(a,b):
    print(a-b)



@my_decorator
def mul(a,b):
    print(a*b)

@my_decorator
def div(a,b):
    print(a/b)


add(10,20)
sub(200,20)
mul(30,20)
div(100,20)