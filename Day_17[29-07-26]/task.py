# Dictionary
# ........................................................
# UPDATE
# d={"name":"SAM", "city":"NY","age":22}

# # replace => 
# d["name"]="Danny"
# print(d)
# #  add => 
# d["fatherName"]="Joe"
# print(d)

# .........................................................
# PROBLEM
# countries = ["India", "France", "Japan", "Canada"]
# capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]

# CCD = {}
# for i in range(len(countries)):
#     CCD[countries[i]] = capitals[i]

# print(CCD)
# ..............................................................
# shop=[9,0,78,45,90,67,89,12]

# DELETE
d={"name":"SAM", "city":"NY","age":22,"fatherName":"Joe"}

# pop("key") => to delete a perticular key-value pair
# d.pop("age")
# print(d)
# .............................................................
# popitem() => to delete the last key-value pair
# d.popitem()
# print(d)
# .............................................................
# clear() => to delete all the key-value pairs
# d.clear()
# print(d)
# .............................................................
# del => delete the dictionary
# del d
# print(d)
# .............................................................
# Functions /inbuilt methods of dictionary

print(d["name"])

# get() => to get the value and also we can provide customize msg
print(d.get("nam","NotExist"))

# keys()
print(d.keys())

# values()
print(d.values())

# for i in d.values():
#     print(i)

# for i in d.keys():
#     print(i)

# items()
print(d.items())

for k, v in d.items():
    print(k,v)