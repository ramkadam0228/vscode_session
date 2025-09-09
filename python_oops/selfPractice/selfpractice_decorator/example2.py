# Question:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

# Hints:

# Use def methodName(self) to define a method.

class circle:
    def __init__(self, r):
        self.r=r
    def areaofcircle(self):
        a = 3.14 *(self.r)*(self.r)
        print(a)

c=circle(5)
c.areaofcircle()