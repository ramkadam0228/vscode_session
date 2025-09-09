# #----------------------------------------#
# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

# Hints:
# Use list comprehension to delete a bunch of element from a list.

# Solution:

li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print li

l2=[x for x in li if x%2 != 0]
print(l2)

#----------------------------------------#
# Question:

# By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.

list1=[12,24,35,70,88,120,155]

flist=[x for x in list1 if x%5!=0 and x%7 !=0]
print(flist)
#----------------------------------------#
# Question:

# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

list2=[12,24,35,70,88,120,155]
final_list=[list2[x] for x in range(len(list2)) if x%2 != 0]
print(final_list)
# ===================================
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print (li)


# =====================================================================
#----------------------------------------#

# Question:

# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# Hints:
# Use list comprehension to make an array.

# Solution:

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print (array)

# ----------------------------------------------------
#----------------------------------------#
# Question:

# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

list3=[12,24,35,70,88,120,155]
# fin_list=[x for (i,x) in enumerate(list3) if i!=0 and i !=4 and i!=5 ]
fin_list=[x for (i,x) in enumerate(list3) if i not in (0,4,5)]
print(fin_list)

# ================================
# Question:

# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# Hints:
# Use list's remove method to delete a value.
list4=[12,24,35,24,88,120,155]
flist=[x for x in list4 if x!=24]

print(flist)

# Question:

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

# Hints:
# Use set() and "&=" to do set intersection operation.

list5=[1,3,6,78,35,55] 
list6=[12,24,35,24,88,120,155]
intersect=[]
for i in list5:
    for j in list6:
        if i == j:
            intersect.append(i)
        else:
            pass

print(intersect)

set1=set(list5)
set2=set(list6)
set1 &= set2
list7=list(set1)
print(list7)