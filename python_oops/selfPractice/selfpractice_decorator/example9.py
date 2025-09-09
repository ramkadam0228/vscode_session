# Please write assert statements to verify that every number in the list [2,4,6,8] is even.



# Hints:
# Use "assert expression" to make assertion.

# input_data=input("Enter even numbers seperated by comma:")
# even=input_data.split(',')
# for i in even:
#         assert int(i)%2==0
#         print(f"Given number {i} is even number")
     

# ------------------------------------------------------------------------------
#----------------------------------------#
# Question:

# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

# Example:
# If the following string is given as input to the program:

# 35+3

# Then, the output of the program should be:

# 38

# Hints:
# Use eval() to evaluate an expression.


# Solution:

# expression = input("Given any operation")

# print (eval(expression))
# -------------------------------------------------------------------
#----------------------------------------#
# Question:

# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


# Hints:
# Use if/elif to deal with conditions.

# list=[1,2,4,6,8,9,33,55,78,98]

# def binarysearch(n):
#     for i in range(0,len(list)):
#         if list[i]==n:
#             print(i)
#         else:
#             print("Number not found in list")
# binarysearch(98)
# ---------------------------------------------------------------------------------------------

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print (bin_search(li,11))
print (bin_search(li,12))
    