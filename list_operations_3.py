#1+2+3+......n
num=[10,20,30,40,50,60]
''' 
#print index use for
for x in num :
    print(x)

#print index use while
index=0
n = len(num)
while index < n :
    print(num[index])
    index=index + 1
'''
#sum all number
sum=0
for x in num :
    sum = sum + x
print(sum)