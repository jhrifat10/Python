#stack=First In, First Out
books = []
books.append("learn c") #append = add
books.append("learn c++")
books.append("learn java")
print(books)
books.pop() # pop = remove
print(books)
books.pop()
print("now the top book is :",books[-1])
books.pop()
if not books:
    print("No books left ")