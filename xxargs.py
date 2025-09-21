#xxargs
#সব argument dictionary আকারে রাখে (key = নাম, value = মান)
def student(**details):
    print(details["name"])

student(id=101,name="anis")