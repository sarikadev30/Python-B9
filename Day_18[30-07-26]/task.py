# x=(5)

# print(x, type(x))


# y={ True:"A", 1:"B", 1.0:"C"}

# print(True==1)
# print(True==1.0)
# print(y)

# ...........................................................
# Functions

# print("Hello World!.....")

# x=34
# y={"name":"Sam","age":34}

# print("Hello World!....")

# print("Lets Start")

# print("Good Morning!....")

# print("Hello World!....")

# def greet():
#     print("Hello World!....")


# greet()
# greet()
# greet()

# def fun():
#     a=23
#     b=67
#     print(a+b)

# fun()

# def addVal(a,b):
#     print(a+b)

# addVal(3,4)
# addVal(13,40)
# .................................................................
# Default Argumented function

# def fun(a,b=9):
#     print(a+b)

# fun(2,3)
# fun(2)
# ................................................................
# Variable Length Argumented Function

# def fun(*x):

#     print(sum(x))

# fun(9,8)
# fun(9,8,9)
# fun(9,8,9,1,2,3,4,5,6)
# ............................................................
# Keyworded Arguments

# def fun(x,y):
#     print(x,y)

# fun(y=8, x=9)
# fun(3,5)

def studentDetails(name, age, city):
    print(f"name => {name} \nage => {age} \ncity=> {city}")


# studentDetails("SAM",23,"NY")
# # studentDetails("SAM","NY",56)
# studentDetails("SAM",city="NY", age=56)
# studentDetails("Joe", age=34, city="NY")
studentDetails("Joe", 34, city="NY")