# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use map() to generate a list.
# Use lambda to define anonymous functions.
input_list= [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda i: i**2, input_list)))

# ==========================================================
# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

print(map(lambda i : i**2, filter(lambda i: i%2==0, input_list)).__doc__)