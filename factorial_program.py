# 1*2*3*4*............*n
a=int(input("Enter the last number :"))
sum=1
for x in range(1,a+1,1):
    sum=sum*x
print(sum)