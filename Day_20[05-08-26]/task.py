# Enclosing Scope


# def outer():
#     msg = "Hello" # "Hi"
#     def inner():
#         msg = "Hi"
#         print("Inner:", msg)

#     inner()
#     print("Outer:", msg)

# outer()	



# outer called 
#  msg="Hello" 
# inner()=>    msg="Hi"  => Inner: "Hi"
# Outer: "Hello"

# def outer():
#     msg = "Hello" # "Hi"
#     def inner():
#         nonlocal msg
#         msg = "Hi"
#         print("Inner:", msg)

#     inner()
#     print("Outer:", msg)

# outer()	

# Outer called 
# msg = "Hello"
# inner() => msg=> "Hi" => Inner: "Hi"
# Outer :"Hi"
# ................................................................

# Global Scope 

# x = 34  # global Scope 
# def printVal():
#     y = 23    # local scoped variable
#     x = 12
#     print(y)
#     print("inside", x)


# printVal()
# # print(y)
# print("outside", x)


# .................................................
# x = 10 # 78

# def valFun():
#     y = 23
#     global x
#     print(x)
#     x = 78
    
#     print(x, y)


# print(x)
# valFun()
# print(x)

# global scope  => x =10

# 10
# local scope for valFun => y=23  
# 10
# localScoped variable x => 78
# 78,23
# 10
# ..........................................................
# Built In Scope


# print(len("PYTHON"))
# .............................................................................

# x = 23
# def fun():
#     x = 78
#     print("3", x)

#     def innerFun():
#         global x
#         x = 56
#         print("4", x)

#     innerFun()
#     print("5", x)

# print("1", x)
# fun()
# print("2", x)

# "1" 23        #global scoped x  =23  => 56
# "3" 78        #local scoped x for fun()
# "4" 56
# "5" 78
# "2" 56

# ...............................................................................

# x = 10


# def my_func():
#     x = 20
#     print(x)


# my_func()
# print(x)
# 20
# 10
# ................................................................................
# x = 100

# def change():
#     global x
#     print(x)
#     x = 200
#     print(x)


# change()
# print(x)
# .................................................................................

# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"

#     inner()
#     print("x inside outer:", x)


# outer()
# # print(x)

# x inside outer: nonlocal 
# ....................................................................................

# x = "global"

# def outer():
#     x = "outer"

#     def inner():
        
#         x = "inner"

#         print("inner:", x)

#     inner()

#     print("outer:", x)


# outer()
# print("global:", x)
# .....................................................................................

