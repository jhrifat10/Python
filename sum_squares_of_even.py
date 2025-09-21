#2^2+ 4^2+6^2
n=int(input("Enter the last even number :"))

sum=0
for i in range(2,n+1,2):
    sum=sum+i**2 # **= square / *=double
print(sum)