n=input("Enter the number : ")
#input 10 20 30=output 60
list =n.split()
sum=0
for num in list:
    sum=sum+int(num)

print(sum)

'''
input() → পুরো লাইনটাকে string আকারে নেয়।
split() → সেই string কে ভেঙে ছোট ছোট আলাদা সংখ্যা (string আকারে) বানায়।
int() → প্রতিটা string কে সংখ্যা (integer) তে রূপান্তর করে।
'''