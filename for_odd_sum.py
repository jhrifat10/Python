#2+4+4........+n
#sum of the even number
num=int(input("Enter the last number :"))
sum=1
for x in  range(2,num+1,2):
    sum=sum+ x
print(sum)
