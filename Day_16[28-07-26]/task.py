# TUPLE

# CRUD
# CREATE
# 1. 
# x=(1,2,4,578,34,13)
# print(x , type(x))

# 2. 
# y=tuple((23,12,12,123,1234,12345))
# print(y, type(y))

# a=[12,23,12,123,12345,45,67,89,10,78,90]

# b={23,45,67,1,2,3,4,5,67,889,90,56,23,45,67}

# res=tuple(a)
# res=tuple(b)
# print(res,type(res))
# ..........................................................................

# READ
x=(1,2,4,578,34,13)

# Loops
# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(i,x[i])
# .........................................
# Indexing
# print(x[0])
# print(x[-2])
# .........................................
# Slicing
# print(x[2:-1:1])
# print(x[0:7])
# print(x[-2:0:-1])

# x = (2, 3, 5, 6, 7, 8, 9, 10)
# # print(x[-3])
# # print(x[5:0:-1])
# print(x[-3:-7:-1])
# ..............................................
# Merging Tuples
# x = (2, 3, 5, 6, 7, 8, 9, 10)
# y = (1,2,4,578,34,13)

# z=x+y
# z=y+x
# print(z, type(z))

# ...............................................

# y = (1,2,4,578,34,13)
# # y.append(67)
# # y[0]=90
# print(y)

# y=list(y)
# y.append(67)
# y=tuple(y)
# print(y,type(y))
# .....................................................
# PROBLEMS............
# nested = (1, 2, (3, 4), [5, 6], {23, 45, 190})
# # nested[3].append(7)
# # nested[3].extend([9, 34, 23, 12])

# nested[4].add(0)
# print(nested)
# ...........................................................................

# DICTIONARY
# CRUD

# CREATE
# x={"name":"Vrishay", "course":"Python","batch":"B-9"}
# print(x, type(x))

# y=dict({"name":"SAM","age":23, "city":"NY"})
# print(y, type(y))

# print(len(y))
# ............................................................
# READ
# print(x["name"])
# print(x["course"])

# # loop 
# for i in x:
#     print(i, x[i])

# for key, value in x.items():
#     print(key, value)

# z={
#     "name":["Sam", "Danny","Joe"],
#     "course":["python","java","c"]
# }
# print(z["name"])
# print(z["name"][2])
# print(z["course"][-3])


# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 32],
#     "income": [90, 75, 80, 93],
# }
# print(f"{d["name"][0]} - {d["age"][0]}")
# print(f"{d["name"][0]} - {d["age"][0]} - {d["income"][0]}")

# for i in d:
#     print(i, d[i][3])

# .............................................................
# x = {"name": "SAM", "age": 23, "city": "NY", "name": "Danny","city":"Delhi"}
# print(x)
# .......................................................................................
