#what is string 
"""
--string are used to store coolection of data.
--string can be represnted by using 3 ways 1. single quote(''), 2.double quote(""),3.triple quote(""" """)
--

"""

name="   rajitha   "
name1="ABHIRAM RATHOD"
message="welcome to python programming"
value=name+message
print("length of value ",len(value))#len() is used to find the length of variable

print("capitalize of sting",name.capitalize())#capitalize()	Converts the first character to upper case

print("convert string to lower case",name1.casefold())#	Converts string into lower case

print("using center method",name.center(10))#returns certain string

print("using count method in string",name.count("a"))#this method is used to count the no.of particula  characters repeated  in a string

print("encode with string",message.encode())#using the encoded version of the string

print("ends with",name.endswith("b"))#it return true or false value

print("expanding tabs",name1.expandtabs(1))#expanding the tab
print("return the trimed version of a string",name.strip())
my_dict={83:67}
print("return translated string",name1.translate(my_dict))
print("using title",message.title())#convert each character first letter into a upper case
print("swap the elements lower to higher or vice versa",name1.swapcase())#swapcase()	Swaps cases, lower case becomes upper case and vice versa




