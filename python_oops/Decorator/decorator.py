"""
decorator in python is allows to modify the behaviour of
another function or method
"""
 
def greet():
    print("Hello good morning")
 
def my_decorator(func):
    print("Before function call")
    func()
    print("After function call")
 
my_decorator(greet)
# output follows like below
# line1: Before function call
# line2: func() here the func name is greet , so greet() will call
#        Hello Good morning
# line3: After function call
 
greet()
# output : Hello good morning
 
"""
the use case is eventhough we called the greet() function alone
i want to get the my_decorator outputs i want to get
"""