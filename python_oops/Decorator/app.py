from deco import my_decorator
class my:

    @my_decorator
    def greet1():
        print("hello good morning")
    """
    "Before function call
    "hello good morning"
    "After function call"
    """
    
    @my_decorator
    def greet2():
        print("Hello good afternoon")
    
    """
    "Before function call
    Hello good afternoon
    "After function call"
    """
    
    @my_decorator
    def greet3():
        print("Good evening")
    
    """
    "Before function call
    Hello good afternoon
    "After function call
    """
    
    greet1()
    greet2()
    greet3()
