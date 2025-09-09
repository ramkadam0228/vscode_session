from deco import my_decorator

@my_decorator
def greet1():
    print("Hello GM")

my_decorator(greet1())