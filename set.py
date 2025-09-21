num1= {1,2,3,4,5,6}
num2=set([5,6,7])
num2.add(8)
num2.remove(8)

print(num2)
#condition
print(4 not in num2)
#union
print(num1 | num2)
# 
print(num1 & num2)
print(num1 - num2)