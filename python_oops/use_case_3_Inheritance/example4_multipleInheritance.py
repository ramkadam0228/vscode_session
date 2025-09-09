"""
multiple inheritance
"""
 
class Flyer:
    def fly(self):
        print("I can fly")
 
class Swimmer:
    def swim(self):
        print("I can swim")
 
class Walker(Flyer,Swimmer):
    def walk(self):
        print("I can walk")
 
Walker().fly()  # Child class access the method of parent class1
Walker().swim()   # Child class access the method of parent class2
Walker().walk()   # Child class access the method of its own
# has context menu