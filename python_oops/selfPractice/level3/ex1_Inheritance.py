# #----------------------------------------#
# Question:

# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.


class person():
    def __init__(self, gender):
        self.gender=gender
    def getgender(self):
        print(self.gender)

class male(person):
    def getgender():
        print("I am male")

class female(person):
    def getgender():
        print("I am female")

p = person('trans')
p.getgender()
male.getgender()
female.getgender()

# ========================================================
#----------------------------------------#
# Question:

# Please write a program which count and print the numbers of each character in a string input by console.

# Example:
# If the following string is given as input to the program:

# abcdefgabc

# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
str='abcdefgabc'
dict={}
for i in str:
    count=0
    pcount=0
    for j in str:
        if i==j:
            count=count+1
        else:
            pass
        dict[i]=count

print(dict)

for i, j in dict.items():
    print(i, j)


# ======================================
# Question:

# Please write a program which accepts a string from console and print it in reverse order.

# Example:
# If the following string is given as input to the program:

# rise to vote sir

# Then, the output of the program should be:

# ris etov ot esir

# Hints:
# Use list[::-1] to iterate a list in a reverse order.
# input_l=input("Enter string to be reversed:")
# # listl=input_l.split(' ')
# print(input_l[::-1])
# =========================================================
# Question:

# Please write a program which accepts a string from console and print the characters that have even indexes.

# Example:
# If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d

# Then, the output of the program should be:

# Helloworld
s='H1e2l3l4o5w6o7r8l9d'
out=[]
out1=[s[x] for x in range(len(s)) if x%2==0]
# for i in range(len(s)):
#     if i%2==0:
#         out.append(s[i])
# print(out1)
# print(s[::2])
# output=str(out1)
# print(output)
output=''
o=''
for i in out1:
    o=output.join(i)
    print(o,end='')

    # ====================================
#----------------------------------------#


# Question:

# Please write a program which prints all permutations of [1,2,3]


# Hints:
# Use itertools.permutations() to get permutations of list.

# Solution:

import itertools
print (list(itertools.permutations([1,2,3])))
# ===========================================
# Question:

# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# Hint:
# Use for loop to iterate all possible solutions.

# Solution:

def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
# solutions=solve(numheads,numlegs)
# print (solutions)
outl=0
import math
def mysol(h,l):
    if l%4 ==0:
        outl= math.floor(l/4)
        print(outl)
    elif (l-1)%4==0:
        outl= math.floor(l/4)
        print(outl)
    elif (l-2)%4==0:
        outl= math.floor(l/4)
        print(outl)
    elif (l-3)%4==0:
        outl= math.floor(l/4)
        print(outl)

    chiken=int(h)-int(outl)
    print(f"No of Chiken are {chiken} and number of rabits is {outl}")
mysol(35,94)

