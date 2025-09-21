n=int(input("Enter the number: "))
m=int(input("Enter the continue/skip point : "))
i=1
while i<n :
    if i==m:
      i += 1
      continue
    print(i)
    i=i+1
