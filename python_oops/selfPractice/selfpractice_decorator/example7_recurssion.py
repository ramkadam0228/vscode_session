# #----------------------------------------#

# Question:


# The Fibonacci Sequence is computed based on the following formula:


# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value of f(n) with a given n input by console.

# Example:
# If the following n is given as input to the program:

# 7

# Then, the output of the program should be:

# 13

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.

# n=eval(input("Enter number for febonacy series:"))
# res=0
# def fun1(n):
#     if n == 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return  fun1(n-1)+fun1(n-2)
       
# r=fun1(n)
# print(r)

# -------------------------------------------
# using list comprihension
# res=0
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        return f(n-1)+f(n-2)

n=eval(input("ENter a number:"))

values= [str(f(x)) for x in range(0,n+1)]

print(values)