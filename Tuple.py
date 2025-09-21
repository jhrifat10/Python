'''
Tuple এর বৈশিষ্ট্য
Ordered → index ব্যবহার করে element access করা যায়
Immutable → একবার বানালে element পরিবর্তন করা যায় না
Loop দিয়ে print করা যায়

{ ... } → Set বা Dictionary হতে পারে
যদি colon : থাকে → dictionary
না থাকলে → set
Tuple → ( ... ) (parentheses)
List → [ ... ] (square brackets)
'''


students=(
    ("jihadul islam",24,45,5,4),
    "rifat ",
    "rabeya begum",
    "nusrat jahan"

)
print(students[0])

for n in students:
    print(n)