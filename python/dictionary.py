#what is dictionary
"""
--it is stores the data in key and value format, the combination of key and value is called as items
--every item is separated with comma(,)
--it is represented by using curly brackets
--it does not allows duplicate values
--it is changable
--we can access the valuse by using key
"""

dict={"name":"rajitha","age":25,"course":"python full stack","salary":34567.00}

print(type(dict))
print(dict)
print(dict.keys())#it displays the keys insid ethe dictionary it returns in list format
print(dict.values())#it displays the vlaues insid ethe dictionary it returns in list format
print(dict.items())#it retuns both key and values in a dictionary

print("updating the dictionary ",dict.update({"name":"ram"}),dict)#updating the value like changing the values

# print("Removes the last inserted key-value pair",dict.popitem())#Removes the last inserted key-value pair
# print("Removes the element with the specified key",dict.pop("name"))#Removes the element with the specified key
print("Returns the value of the specified key",dict.get("name"))#Returns the value of the specified key

print("Returns a dictionary with the specified keys and value",dict.fromkeys(dict))#Returns a dictionary with the specified keys and value

print("remove complete dictionary",dict.clear())#this method is used to clear the dictionary