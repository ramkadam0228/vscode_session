def my_decorator(name):
        def wrapper():
            print("Before function call")
            name()
            print("After function call")
        return(wrapper)