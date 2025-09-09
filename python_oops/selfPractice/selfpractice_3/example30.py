# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

# Hints:

# Use [n1:n2] notation to get a slice from a tuple.

# # Solution

def print2lines():
    tuple1=(1,2,3,4,5,6,7,8,9,10)
    print(tuple1[:5])
    print(tuple1[5:])

print2lines()    

#=================================================================================
# Question:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

# Hints:

# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.
out=[]
outt=()
tuple1=(1,2,3,4,5,6,7,8,9,10)
for i in tuple1:
    if i % 2 ==0:
        out.append(i)

print(tuple(out))