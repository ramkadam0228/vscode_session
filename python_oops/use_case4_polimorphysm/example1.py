class Dog:
    def speak(self):
        print("Barks")

class Cat:
    def speak(self):
        print("Meow")

"""Both Cat and Dog has speak function but their implementation is different"""

def animal_sound(animal):
    print(animal.speak())

# Dog().speak()
# Cat().speak()
dog=Dog()
cat=Cat()
animal_sound(dog)
animal_sound(cat)
