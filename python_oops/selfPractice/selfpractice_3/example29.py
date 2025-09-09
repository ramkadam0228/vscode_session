# # #----------------------------------------#
# # 2.10

# # Question:
# # Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# # Hints:

# # Use ** operator to get power of a number.
# # Use range() for loops.
# # Use list.append() to add values into a list.
# # Use [n1:n2] to slice a list


out_list=[]
def sqrfunc():
    for i in range(1,21):
        res=i**2
        out_list.append(res)
    print(out_list[-5:len(out_list)])



sqrfunc()

# #===============================================================================================
# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# # Use [n1:n2] to slice a list

out_list=[]
def sqrfunc():
    for i in range(1,21):
        res=i**2
        out_list.append(res)
    print(out_list[5:])



sqrfunc()

#=======================================================================================================
# Question:
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

# Hints:

# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.

# Solution
out_list=()
out=[]
def sqrfunc():
    for i in range(1,21):
        res=i**2
        out.append(res)
        out_list=tuple(out)
    print(out_list)    



sqrfunc()