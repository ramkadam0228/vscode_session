# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input_data=input("Enter combination of text and numbers: ")
dict={"DIGIT": 0, "ALPHABET":0,"SPECIAL_CHAR":0}
a=0
b=0
c=0
for i in input_data:
    print(i)
    if i.isdigit():
        dict["DIGIT"]+=1
        
    elif i.isalpha():
        dict["ALPHABET"]+=1
        
    else:
        i.isascii()
        dict["SPECIAL_CHAR"]+=1      

print(dict)