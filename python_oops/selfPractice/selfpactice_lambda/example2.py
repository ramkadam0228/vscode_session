# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


input_list=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x**2, filter(lambda x: x%2==0,input_list) )))

################################################################################
# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:

# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.
input_list=[]
for i in range(0,20):
    input_list.append(i)


print(list(filter(lambda x:x%2==0,input_list)))
print(list(filter(lambda x:x%2==0, range(0,20))))  # here you can directly give range in the place of list

################################################################################################
# Question:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# Hints:

# Use map() to generate a list.
# Use lambda to define anonymous functions.

print(list(map(lambda x:x**2,range(1,21))))