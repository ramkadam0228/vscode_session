# Question:

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

# Example:
# If the following words is given as input to the program:

# 2 cats and 3 dogs.

# Then, the output of the program should be:

# ['2', '3']

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:

# Use re.findall() to find all substring using regex.
# import re
# input_data=input("Enter Data as digit followded by String:")
# # format="(\d+) (\W+)"
# print(re.findall("\d+",input_data))
# print(re.findall("\w+",input_data))
# --------------------------------------------------------------------------------
# Print a unicode string "hello world".

# Hints:

# Use u'strings' format to define unicode string.
# unicodeprinting=u"Hello world!"
# print(unicodeprinting)
# -----------------------------------------------------------------------------
#----------------------------------------#
# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# Hints:

# Use unicode() function to convert.

# Solution:

s = input("Enter some text:")
uni = UnicodeDecodeError (s ,"utf-8")
print (uni)
