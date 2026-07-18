# FOR LOOP with Break

# for i in range(1,6):
#     if i==3:
#         break
#     print("Guest: ", i)

# ..........................................................
# for guest in range(1, 6):
#     print("Guest", guest)
#     if guest == 4:
#         break
# ..........................................................
# For loop with continue

# for i in range(1, 8):
#     if i == 5:
#         continue
#     print("Guest", i)
# ...................................................................
# Problem 

# count = 1
# for k in range(1, 10):  
#     if k == 5:
#         continue
#     count += 1

# print(count) 

# DRY RUN 
# c=1
#  k => 1 2 3 4 5 6 7 8 9
# k=1 1==5 => F c=1+1=2
# k=2 2==5 => F c=2+1=3
# k=3 3==5 => F c=3+1=4
# k=4 4==5 => F c=4+1=5
# k=5 5==5 => T continue....
# k=6 6==5 => F c=5+1=6
# k=7 7==5 => F c=6+1=7
# k=8 8==5 => F c=7+1=8
# k=9 9==5 => F c=8+1=9
# k=10 .....
# 9
# .................................................................

# NESTED LOOPS => loop inside the loop

# for i in range(1,6):      # 1 2 3 4 5
#     for j in range(1,5):  # 1 2 3 4
#         print("Family ",i , "ate", j, "Candy")

# ..........................................................

# i=1
# while i<=5:
#     j=1
#     while j<=4:
#         print("Family",i,"ate",j , "candies")
#         j+=1
#     i+=1
# ...........................................................

# Father gave the son a target, of completing 10 sets. Each set contains 10 Rounds of a field.

# ..............................................................................

"""
**********
**********
**********
**********
**********
"""

r=5
c=10 
for i in range(r):  # 0 1 2 3 4
    for j in range(c): # 0 1 2 3 4 5 6 7 8 9
        print("*",end="")
    print()


"""
1111111111
2222222222
3333333333
4444444444
5555555555
"""