"""
I want to use parent class methods in the child class
we need to use a super()
 
in Animal we have two classes
     1.speak   2.greet
 
in Dog we have one class
    1.speak
 
now i want to use greet(parentclass) inside the child class
"""
 
"""
inheritance:
  It allows to define a class that inherits all the methods
  and properties from another calss
 
basically the idea is there is calss : parent class
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
 
    def greet(self):
        print("this is inheritance")
 
# step-2: create the child class
class Dog(Animal):
    def speak1(self):
        # here i want to use greet
        super().greet()
        super().speak()
        print(f"{self.name} barks")
 
 
Dog('snoopy').speak1()
"""
Dog is calling speak1 function
inside speak1
   it is calling greet() : this is inheritance
   after that : snoopy barks
"""
 
 
