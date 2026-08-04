
# factorial  5! => 5*4*3*2*1

# def factorial(n):
#     i=1
#     fact=1
#     while i<=n:
#         fact*=i
#         i+=1
#     print(fact)


# factorial(0)
# .............................................................

# print vs return 

# def factorial(n):
#     i=1
#     fact=1
#     while i<=n:
#         fact*=i
#         i+=1
#     return fact


# # x=factorial(7)
# # print(x)

# print(factorial(3))

# .................................................................................


# 0 1 1 2 3 5 8 13 21 .............

# def fibonacciSeries(n):
#     a=0
#     b=1
#     res=[]

#     for i in range(n):   # 0 1 2 3 
#         res.append(a)    #[0]
#         c=a+b
#         a=b
#         b=c
#     return res

# print(fibonacciSeries(4))

# a=0  b=1 
# i =>  0 1 2 3 
# i=0   res=[0]  c=0+1=1   a=b=> a=1  b=c=> b=1
# i=1   res=[0,1] c=1+1=2  a=b=> a=1  b=c => b=2
# i=2   res=[0,1,1] c=1+2=3 a=b=> a=2  b=c=> b=3
# i=3   res=[0,1,1,2] c=2+3=5 a=b=> a=3 b=c => b=5
# return res res=[0,1,1,2]

# a=[1,2,3,4,5,6] 
# 0   n-1
# [6,5,4,3,2,1]

# def reverseList(res):
#     ans=[]
#     x=len(res)-1
#     for i in range(x,-1,-1):
#         ans.append(res[i])
#     print(ans)
# .............................................
# def reverseList(res):
#     x=res[::-1]
#     print(x)
# .............................................
# def reverseList(res):
#     res.reverse()
#     print(res)


# a=[1,2,3,4,5,6]
# print(a)
# reverseList(a)
# .............................................................................

# SCOPE of a variable

# Local Scope => Enclosing Scope => Global Scope => Built in Scope 


# def greetPeople():
#     msg="Hello User"     # Local Scope 
#     print(msg)

# greetPeople()
# print(msg)

# Enclosing Scope


# def outer():
#     msg = "Hello"

#     def inner():
#         nonlocal msg
#         msg = "Hi"
#         print("Inner:", msg)

#     inner()
#     print("Outer:", msg)

# outer()	
