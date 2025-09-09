def my_decorator(func):
    def wrapper(a,b):
        print("Before function call")
        func(a,b)
        print("After function call")
    return(wrapper)

