"""
we created two classes
two calles has same function name
but not same function behaviour
when classes are different function behaviour also different
eventhough functions has same name in two classes
"""
class Dog:
    def speak(self,name):
        print(f"{name} barks")
 
class Cat:
    def speak(self,name):
        print(f"{name} meow")
 
 
Dog().speak('Snoopy')
Cat().speak('buddy')
 