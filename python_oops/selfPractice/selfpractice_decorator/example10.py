# #----------------------------------------#
# Question:

# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.



# Hints:
# Use random.choice() to a random element from a list.


# Solution:

import random

# print(random.randint(1,10))
# print(random.choice([2,4,6]))

print(random.choice([i for i in range(11) if i%2==0]))  #-- Any number out of the result will be displayed
print(([i for i in range(11) if i%2==0]))

print(random.choice([i for i in range(121) if i%5==0 and i%7==0]))
print(random.randint(100,200))
print(random.sample([i for i in range(100,200) if i%2==0],5))
print(random.sample([i for i in range(1,1000) if i%5==0 and i%7==0],5))
print(random.randrange(2,9))