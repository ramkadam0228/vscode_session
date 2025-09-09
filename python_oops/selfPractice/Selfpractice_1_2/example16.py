# #----------------------------------------#
# Question 16
# Level 2

# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

input_list=input("Enter numbers: ")
# list=input_list.split(',')
out_list=[]
numbers= [(eval(i)*eval(i)) for i in input_list.split(',') if (int(i)%2 != 0)]
# for i in range(len(list)):
#     if (eval(list[i]))%2 != 0:
#         a=eval(list[i])*eval(list[i])
#         out_list.append(a)
print(numbers)
