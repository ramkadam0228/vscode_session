# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input_data=input("Enter correct password: \n")
data=input_data.split(',')
   


count=0

for i in data:
    dict={"digit":0, "LChar":0,"UChar":0,"ascii":0}
    for j in i:
        
        if len(i) > 6 and len(i) < 12:
            if j.isdigit(): 
                # print("Valid Number")
                dict["digit"] = 1
            elif j.islower():
                # print("Valid Char")
                dict["LChar"] = 1
            elif j.isupper():
                # print("Valid Char")
                dict["UChar"] = 1
            elif j.isascii():
                # print("Valid Special char")
                dict["ascii"] = 1
    
    print(dict)
    if dict["digit"] == 1 and dict["LChar"] == 1 and dict["UChar"] == 1 and dict["ascii"] == 1:
        print(i)

    

# for val in dict.values():
#     if val == 1:
#         # print("Password is valid")
#         # print(input_data)
#         count+=1
#     # else:
#     #     print("Invalid password")
#     #     break
# # print(dict)
# if count==4:
#     print(" Below are valid passwords ")
#     print(input_data)




