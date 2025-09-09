
# Question:

# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 100

# Then, the output of the program should be:

# 0,35,70

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question, it should be assumed to be a console input.

input_data=int(input("Enter a number"))
values=[]
def div(input_data):
    for i in range(0,input_data+1):
        if i%5==0 and i%7==0:
            # values.append(i)
            
            yield i
        else:
            pass
            
for i in div(input_data):
    print(i)
    values.append(i)

# div(input_data)
print(values)

# Return:
# Terminates the function: When a return statement is encountered, the function immediately exits, and the returned value is passed back to the caller.
# Returns a single value: A function can return only one value using return.
# Suitable for simple functions: return is ideal when you want to compute a result and return it directly.

# Yield:
# Pauses the function:
# When a yield statement is encountered, the function's state is saved, and the yielded value is returned to the caller.
# Creates a generator:
# A function that contains yield is known as a generator function. When called, it returns a generator object, which can be iterated over.
# Returns multiple values:
# A generator can yield multiple values, one at a time, allowing for efficient processing of large datasets or infinite sequences.