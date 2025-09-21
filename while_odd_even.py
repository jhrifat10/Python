n = int(input("Enter the last term: "))
i = 1

while i <= n:
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")
    i =i + 1
