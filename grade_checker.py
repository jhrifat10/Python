marks=int(input("enter your marks 0-100 :"))
if marks > 100 or marks < 0 :
    print("Invalid marks")
elif marks>=80:
    print("A+")
elif marks>=70:
    print("A")
elif marks>=60:
    print("A-")
elif marks>=50:
    print("B")
elif marks>=40:
    print("C")
elif marks>=33:
    print("D")
else:
    print("F")


