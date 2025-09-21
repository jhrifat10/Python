#1^2 + 2^2 + 3^3 ......n^2

n=int(input("Enter the digit : "))
sum=0
for i in range(1,n+1):
    sum+=i*2
print(sum)