studentId={
    "101" : "jihadul islam",
    "102" : "sriti islam",
    "103" : "nahidul islm",
    "104" : "istak hossen"
}
print(studentId["101"])
#all key
print(studentId.keys())
# all values
print(studentId.values())

#add new entry
studentId["105"] = "rahim islam"
print(studentId)

for key, value in studentId.items():
    print(key, ":", value) # key and value print 
