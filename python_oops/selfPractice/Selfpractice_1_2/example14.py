# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input_date=input("Enter text in lower and upper case: ")
a=b=c=0
dict={"UPPERCASE":0,"LOWERCASE":0,"NUMBER":0,"ASCII":0}
for i in input_date:
    
    if i.isupper():
        dict["UPPERCASE"]+=1
    elif i.islower():
        dict["LOWERCASE"]+=1
    elif i.isdigit():
        dict["NUMBER"]+=1
    else:
        dict["ASCII"]+=1
print(dict)    

        
