n=int(input("Enter the last value :"))
sum=0

for x in range(2,n+1,2):
    sum=sum + x**x
print(sum)