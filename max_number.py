num1=int(input("enter num1 number "))
num2=int(input("enter num2 number "))
num3=int(input("enter num3 number "))

if num1>num2 and num1>num3:
    print("maximum of a number is",num1)
elif num2>num1 and num2>num3:
    print("maximum of a number is",num2)
else:
    print("maximum of a number is",num3)
    