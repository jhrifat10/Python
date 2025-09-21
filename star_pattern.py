"""
Qustion-1
*
**
***
***

n=3
for i in range(n+1):
    print(i*"*")
 """
'''
Qustion-2
*
***
*****

n=int(input("enter the row:"))
for i in range(n+1):
    print((2*i-1)*"*")
'''
'''
Qustion-3
    *   
   **
  ***
 **** 
*****
'''
'''
n=int(input("Enter the row :"))
for x in range(1,n+1):
    print(" "*(n-x)+"*" * x)
''' 
 #piramid
n=int(input("Enter the row :"))
for i in range(1,n+1):
     print(" "*(n-i)+"*" * (2*i-1))
