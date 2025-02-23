#what is string formating
"""
String formatting in Python is the process of inserting or embedding variables, expressions, or values into a string in a structured and readable manner. It allows dynamic text generation by replacing placeholders with actual values.

Python provides multiple ways to format strings, including:

f-strings (f"...") – The most modern and recommended approach.
.format() method – Allows flexible formatting using placeholders {}.
% formatting – An older method using % operators (not recommended).
Template Strings – A safer way using placeholders like $name, useful in certain cases.
"""

name="rajitha"
age=25
salary=34567
print("my name is {}.am {} years old.".format(name,age))
print(f"my name is {name}. am {age} years old.i got salary{salary}")
print("my name is %s.am %d years old.i got salary %d"%(name,age,salary))

from string import Template

t = Template("My name is $name and I am $age years old.")
print(t.substitute(name="David", age=40))