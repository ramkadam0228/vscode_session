# Question:

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# john

# In case of input data being supplied to the question, it should be assumed to be a console input.

# Hints:

# Use \w to match letters.

input_data=input("Enter email ID:")
n=input_data.split('.')
fname=n[0]
name=n[1].split('@')
sname=name[0]
cname=name[1]


print(f"My name is {fname} surname is {sname} and i work for {cname}")


import re
emailAddress = input("Enter email ID:")
pat2 = "(\w+).(\w+)@((\w+).(\w+))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))
print (r2.group(2))
print (r2.group(3))