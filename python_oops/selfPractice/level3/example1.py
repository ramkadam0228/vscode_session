# #----------------------------------------#
# Question:

# Please write a program to print the running time of execution of "1+1" for 100 times.

# Hints:
# Use timeit() function to measure the running time.

# from timeit import Timer

# t=Timer("for i in range(100): 1+1 ")
# print(t.timeit())
#----------------------------------------##----------------------------------------#
# Question:

# Please write a program to shuffle and print the list [3,6,7,8].
# Hints:
# Use shuffle() function to shuffle a list.

# from random import shuffle
# list=[3,6,7,8]
# # print(shuffle(list)) This is not printable. shuffle works on original list
# print(list)
#----------------------------------------##----------------------------------------#
# Question:

# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# Hints:
# Use list[index] notation to get a element from a list.
subject=["I", "You"]
verb=["Play", "Love"]
object=["Hockey","Football"]

# user_input=input("Enter some sentences:")

# words=user_input.split(' ')
for i in range(len(subject)):
    for j in range(len(verb)):
        for k in range(len(object)):
            sentence="%s %s %s" % (subject[i], verb[j], object[k] )
            print(sentence)

