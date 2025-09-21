
mark =int(input(" Enter your marks 0-100 : "))
if mark < 0 or mark > 100:
    print("Invalid marks! Please enter between 0 to 100.")
elif mark >= 80 and mark <= 100:
    print("A+")
elif mark >= 70 and mark <= 79:
    print("A")
elif mark >= 60 and mark <= 69:
    print("A-")
elif mark >= 50 and mark <= 59:
    print("B")
elif mark >= 40 and mark <= 49:
    print("C")
elif mark >= 33 and mark <= 39:
    print("D")
else:
    print("Fail")
