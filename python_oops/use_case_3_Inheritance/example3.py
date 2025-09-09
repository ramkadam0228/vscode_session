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
class WildAnimal:
    def __init__(self, color, name):
        self.color=color
        self.name=name

    def animalcolor(self):
        print(f"{self.color} color of Animal")

class Animal:
    def __init__(self,name):
        self.name=name
 
    def speak(self):
        print(f"{self.name} makes a sound")

    def greet(self):
        print("I am in inheritance")
 
# step-2: create the child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class puppy(WildAnimal):
    def speak(self):
        print(f"{self.name} silent")  
        # print (f"{self.color}")      
 
Animal('cow').speak()
Dog('snoopy').speak()
Dog('snoopy').greet()
# puppy('uouo').speak()
puppy('Pink','AA').animalcolor()
# puppy('pink','Kuku').animalcolor()



"""
observation-1:  Child class Dog able to use attribute of parent class
observation-2: child class Dog able to modify the behaviour of
               function which is available in parent class
               This is called method overwriding
               Parent class: Animal : speak : makes a sound
               Child class : Dog    : speak : barks
Observation-3: Parnt class has a method
               Partnt class : Animal : greet
               is greet method able to call be child class (DOG): yes
               
"""