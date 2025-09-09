class Animal:
    def speak(self):
        print("Some Sound")

#Child 1
class Dog(Animal):
    def speak(self):
        print("Barks")
#Child 2
class Cat(Animal):
    def speak(self):
        print("Meow")


animals=[Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()