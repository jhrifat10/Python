# 1*1 + 2*2 + 3*3 ......n*n
'''
n = 3
x*x → 1² + 2² + 3² = 14
x**x → 1¹ + 2² + 3³ = 32

'''
n=int(input("Enter the last number : "))
sum=0
for x in range(2,n+1,1): #range (start,stop,base)
    sum=sum+x*x
print(sum)