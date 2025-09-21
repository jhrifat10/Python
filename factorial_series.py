## 1! + 2! + 3! + ... + n!
'''
1! = 1 → sum = 1
2! = 1 × 2 = 2 → sum = 1 + 2 = 3
3! = 1 × 2 × 3 = 6 → sum = 3 + 6 = 9
4! = 1 × 2 × 3 × 4 = 24 → sum = 9 + 24 = 33
5! = 1 × 2 × 3 × 4 × 5 = 120 → sum = 33 + 120 = 153
'''
n = int(input("Enter the last number: "))
total = 0

for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact = fact * j
    total = total + fact      

print("Factorial Series Sum =", total)
