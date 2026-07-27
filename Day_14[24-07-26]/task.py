# LIST
# DELETE


# pop : where deletion is based on index
# z = [23, 45, 67, 89, 12, 34, 11, 12, 13, 14, 15]

# print(z, len(z))
# # z.pop(4)
# # z.pop(-2)
# # print(z,len(z))
# z.pop()               #NOTE :  if index is not provided , it will remove the last element
# print(z,len(z))
# .....................................................
# remove : where deletion is based on value

# z = [23, 45, 67, 89, 12, 34, 11, 12, 13, 14, 15]
# print(z, len(z))
# z.remove(34)
# print(z, len(z))
# z.remove(12)          #NOTE : If multiple occurances are there, remove function will remove the first occurance only
# print(z, len(z))

# ..........................................................................................
# PROBLEMS
# 1.
# stationary = []
# stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()
# print(stationary)
# .............................................
# 2.
# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman"]
# for i in range(len(movies)):
#     if i == 3:
#         break
#     print(movies[i])
# .............................................
# 3.
# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman", "Thor", "Avengers"]
# for i in range(len(movies)):
#     if i == 2 or i == 4:
#         continue
#     print(movies[i])
# ..................................................................................
# INBUILT FUNCTIONS OF LIST

movies = ["bahubali", "Spider-Man", "Iron Man", "Superman", "Thor", "Avengers"]

# len() => which give me the number of elements
print(len(movies))

# sum(list) => gives the sum of all elements of the list

z = [1, 2, 3, 4,9, 5, 6, 7, 8]
print(sum(z))
# logic
# ds=0
# for i in range(len(z)):
#     ds+=z[i]

# print(ds)
# .................................................
# max(list) => gives the maximum no. in the list
print(max(z))
# logic
# z=[4,7,8,0]
# m=z[0]
# for i in range(1,len(z)):
#     if z[i]>m:
#         m=z[i]

# print(m)

# m=4
# i=1 => 3
# i=1 z[i]=7 7>4 => True => m=z[1]=7
# i=2 z[i]=8 8>7 => True => m=z[2]=8
# i=3 z[i]=0 0>8 => False =>...
# print(m)=> 8
# .................................................
# min(list) =>  gives the minimum no. in the list
z=[4,7,8,0]
# print(min(z))
# m=z[0]
# for i in range(1,len(z)):
#     if z[i]<m:
#         m=z[i]

# print(m)
# ..................................................
# index(value) : to get the index of the particular element
z=[4,7,8,0]
# print(z.index(8))

val=8
for i in range(len(z)):
    if z[i]==val:
        print(i)
        break


# .........................................................................................