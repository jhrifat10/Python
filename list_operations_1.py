strings=["ab","abs","abss","abc","abcc","abcd"]

print(len(strings)) #print length

print(strings[2]) # print the 3rd item (index 2) from the list

print(strings[-1]) #negative index print "abcc" (last item)

strings.append("ab") #add a new item at the end of the list.
print(strings)

strings.insert(2,"Rifat") #insert a new value after index 2
print(strings)

strings.remove("abcc") #remove strings abcc
print(strings)

