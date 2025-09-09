# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# Hints:

# To override a method in super class, we can define a method with the same name in the super class.

class Shape():
    def __init__(self):
        pass
    def area():
        return 0
class squre(Shape):
    def __init__(self, l):
        # super().__init__()
        self.l=l
    def area(self):
        
        super().area
        return(self.l*self.l)
print(squre(4).area())
    
    # --------------------------

# Please raise a RuntimeError exception.

# Hints:

# Use raise() to raise an exception.

# Solution:

def throws():
    return 5/0

try:
    throws()
# except ZeroDivisionError:
#     print("division by zero!")
except Exception as err:
    print ('Caught an exception', err)
finally:
    print ('In finally block for cleanup')


# =================================================================
# Define a custom exception class which takes a string message as attribute.

# Hints:

# To define a custom exception, we need to define a class inherited from Exception.

# Solution:

class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
print(error)