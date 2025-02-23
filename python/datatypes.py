#data types in python
"""
variable can store data on different types, and diffent types can do diifferent things
 --in python we have two types of data types
 1.basic(primitive type):primitive means already defined (integer,float,boolean,complex)
 2.advanced(non-primitive type):user can defined(list,tuple,strings,disctionary,set)
"""

#integer type data type
"""
it stores data in numbers only
Int, or integer, is a whole number, positive or negative, 
without decimals, of unlimited length.
"""

#examples

a=10
print(type(a))
b=20
print(type(b))
ab=a+b
print(type(ab))
bc=a+ab
print(type(bc))


#float data type

"""
Float, or "floating point number" is a number, 
positive or negative, containing one or more decimals.
"""

# float examples

abhi=12.90
print(abhi)
raj=12.65
print(raj)
vikky=abhi+raj
print(vikky)
ram=vikky+abhi
print(ram)


#boolean datatype
""" boolean datatype displays the values in true or false"""

#boolean exaplems

aara=True
print(aara)
abhi=False
print(abhi)
raj=aara+1
print(raj)
ram=aara-1
print(ram)


#complex datatype
"""complex datatype is nothing but combination of real number and imaginary number
-- complex datatype=realnumber+imaginary number j
 

"""


a=1+0j
print(type(a))
b=23+3j
print(type(b))

c=12+4j
print(type(c))
