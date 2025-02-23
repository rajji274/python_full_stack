#what is tuple
"""
A tuple is a collection similar to a Python list.
 The primary difference is that we cannot modify a tuple once it is created.
--separated with cammas (,)
--We create a tuple by placing items inside parentheses ()
Ordered - They maintain the order of elements.
Immutable - They cannot be changed after creation.
Allow duplicates - They can contain duplicate values.
Each item in a tuple is associated with a number, known as a index.
"""


tup=("hi",1,"welcome","abhi","ram")

print("length of tupple",len(tup))#finding the length of variable

for tup1 in tup:#iterable method in tupple
    print(tup1)

print("applying count method",tup.count(1))#count the no.of items repeated in a tuple

print("applying index method",tup[2])#Searches the tuple for a specified value and returns the position of where it was found