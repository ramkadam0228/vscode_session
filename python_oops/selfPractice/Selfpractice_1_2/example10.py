# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.


# list=[]
# final_list=[]
# input_sentences=input("Enter text: ")
# list=input_sentences.split(' ')
# set={}
# set=sorted(list)
# final_set={}
# # set{}
# # print(set)
# j=0
# for i in range(0,len(set)):
#         for j in range(i, len(set)):
#             if i==j:
#                final_list.append(set[i])  
#                break
#             elif set[i] != set[j]:
#                final_list.append(set[j])
#                break
#             else:
#                  pass

# final_list=list(set(final_list))
# print(final_list, end=' ')


list=[]
final_list=[]
input_sentences=input("Enter text: ")
list=input_sentences.split(' ')
set={}
set=sorted(list)

for i in set:
        if i not in final_list:
                final_list.append(i)

print(final_list)
