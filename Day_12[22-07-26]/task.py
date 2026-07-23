"""
....*
...***
..*****
.*******
*********
"""
n=5
# i          spaces                       stars
# i=1          4     (n-i)                  1       (2*i-1) => 1
# i=2          3                            3               => 3
# i=3          2                            5               => 5
# i=4          1                            7               => 7
# i=5          0                            9               => 9


# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()

# .............................................................................................
# DATA TYPES

# s="SAM"

# print(s[1])
# # s[1]="R"
# # print(s[1])
# # print(s)


# t=["SAm","Danny","Sonu"]
# t[0]="RAM"
# print(t)

# .....................................................................
# NON Primitive Data types:

# LIST

# CRUD => CREATE  READ  UPDATE    DELETE
# .............................................
# CREATE

# 1. 
# x=[1,2,3,4,5,6,7,8]
# print(x, type(x))

# 2. 
# y=list(("Sam","Danny", "Joe", "Jenny"))
# print(y, type(y))

# ..............................................
# READ
# x=[1,2,3,4,5,89,67,23,12,345,678]
# Positive Indexing => 0 - (n-1)      L => R
# Negative Indexing => n -  (-1)      R => L

# x=[1, 2, 3, 4, 5, 89, 67, 23, 12, 345, 678]
#  0  1  2  3  4   5  6    7   8   9    10
#-11 -10 -9 -8 -7 -6  -5  -4  -3  -2    -1
# print(len(x))
# print(x[7])
# print(x[9])
# print(x[1])
# print(x[-4])

# z = [1, 2, 3, 4, "Sam", 3.4, True, False, 54.90]
# print(z[4], z[-2])

# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]
# print(K[-1])
# print(K[-1][2])
# print(K[-4])

# LOOP
# z = [1, 2, 3, 4, "Sam", 3.4, True, False, 54.90]

# # Loop over the elements
# for i in z:
#     print(i)

# # Loop over the index
# for i in range(len(z)):
#     print(i, z[i])

# ................................................................
# SLicing
# Syntax   nameOfTheList[start : stop : step] # start = 0 step = 1

z = [1, 2, 3, 4, "Sam", 3.4, True, False, 54.90]

print(z[4:7])

# z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23]

# print(z[2:5:1])  # end => end-1
# print(z[:3:2])  # start default=0
# print(z[:5:])  # step default=1
# print(z[6::-1])
# print(z[6::1])
# print(z[6::])
# print(z[-2::-1])