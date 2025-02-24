marks=int(input("enter students marks upto 100"))


if marks>100:
    print("enter wrong marks marks max is 100",marks)
elif marks<100 and marks>90:
    print("A++ Grade",marks)
elif marks<90 and marks>80:
    print("A Grade",marks)
elif marks<80 and marks>70:
    print("B++ Grade",marks)
elif marks<70 and marks>60:
    print("B Grade",marks)
elif marks<60 and marks>50:
    print("C Grade",marks)
else:
    print("Failed ",marks)