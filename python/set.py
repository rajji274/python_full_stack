#what is set
"""
--Sets are used to store multiple items in a single variable.
--set is represented by {}
--A set is a collection which is unordered, unchangeable*, and unindexed.
-- Note: Set items are unchangeable, but you can remove items and add new items.


"""

set1={1,2,3,4,5,6,782,12,1,2,3}
print(set1)
print(type(set1))
set1.add(14)#this method is used to add element in a set
print(set1,"after adding elemnets to set")
set2=set1.copy()#this method is used to copy the existing set to new one
print("set2 copied data",set2)
print("clearing set2",set2.clear())#this method is used to clear the set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)#Returns a set containing the difference between two or more sets
print("difference of two sets",z)
data=x.difference_update(y)#	Removes the items in this set that are also included in another, specified set
print("difference of two sets",data)
# print("removing the element",x.discard("banana"),x)#	Remove the specified item
ab=x.intersection(y)#Returns a set, that is the intersection of two other sets
print("intersection of a elements",ab)
