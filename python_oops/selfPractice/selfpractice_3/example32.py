# Question:
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.
out=[]
input_data=[1,2,3,4,5,6,7,8,9,10]
# x=lambda i: i if (i%2==0 ) else print("odd")
# for i in input:
#     a=x(i)
#     out.append(a)

# print(out)    
# list(map(lambda i : i if (i%2==0) else print("Odd"),input_data))
print(list(filter(lambda i : (i%2)==0, input_data)))
odd=(filter(lambda i : (i%2)!=0, input_data))
print(odd)

