def my_decorator(func):
    def wrapper(a,b):
        print("Before function call")
        func(a,b)
        print("After function call")
    return(wrapper)

def decorator2(message):
    def my_decorator(func):
        def wrapper(a,b):
            print("Before function call")
            func(a,b)
            print("After function call")
        return(wrapper)
    return(my_decorator)


@my_decorator 
def add(a,b):
    print(a+b)


add(10,20)