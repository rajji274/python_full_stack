#what is list
"""
list is collection of data.
it can be represented by square brackets  []
list is immuatable
list allows duplicate values
List items are ordered, changeable, and allow duplicate values.
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
List items are indexed, the first item has index [0], the second item has index [1]
"""


list=[1,2,3,4,1,3,6,7,4,3,9]
print(len(list))
list1=["hi","hello","welcome"]
print(list+list1)
list1.append("tesk")#append(): this method is used to add the items in a list
print("after adding elemenets in a list",list1)

#list.clear()#this method is used to clear the all items in a list
print("after clearing the data list",list)

list1.copy()#retrun the copy of a list
print("after copy the list",list1)

list.count(1)#this method is used to count the number 
print("counting the number",list.count(1))
list3=[12,13,45,42]
list1.extend(list3)	#Add the elements of a list (or any iterable), to the end of the current list
print("extending/adding  the elements",list1)

list1.index("hi")#	Returns the index of the first element with the specified value
print("after using index method",list1.index("hi"))

list3.insert(2,"hello")#	Adds an element at the specified position
print("after inserting values in list",list3)

print("removing elements",list3.pop())#	Removes the element at the specified position

list1.remove("hi")#	Removes the first item with the specified value
print("after applying remove method",list1)
l=list.reverse()
print("applying the revers a list",l)#this method is used to revers a list
l1=list.sort()
print("applying sort method in list",l1)

print(list1[1])
print(list1[0])
print(list1[-3])
print(list[1:4])
print()