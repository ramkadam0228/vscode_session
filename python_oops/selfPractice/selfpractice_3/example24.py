# #----------------------------------------#
# Question 24
# Level 1

# Question:
#     Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
#     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#     And add document for your own function
    
# Hints:
#     The built-in document method is __doc__
# print (abs.__doc__)
# print (int.__doc__)
# print (input.__doc__)


def squreRam(n):
    ''' This function gives squre of given number '''
    return n**2


print(2)

print(squreRam.__doc__)

output={}
# print(output.__annotations__.__doc__)
print(output.__contains__.__doc__)