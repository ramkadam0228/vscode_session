"""
inheritance:
  It allows to define a class that inherits all the methods
  and properties from another calss
 
basically the idea is there is class : parent class
parent class has some variable/attributes and have some methods
 
now we will create some child class
child class can use the attributes and methods of a parentclass
"""
 
# step-1: create a parent class
# one attribute: name
# two methods one is __init__, speak
 
class Animal:
    def __init__(self,name):
        self.name=name
 
    def speak(self):
        print(f"{self.name} makes a sound")
 
 
Animal('cow').speak()  # name='cow'

