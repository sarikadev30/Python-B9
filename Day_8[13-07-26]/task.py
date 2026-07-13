# Loops
# print("Hello World....")
# print("Hello World....")
# print("Hello World....")
# print("Hello World....")
# print("Hello World....")

#  loops => while loop , for loop, do-while loop

# i=1
# while i<=5:
#     print("Hello World....")
#     i+=1

# DRY RUN
# i=1   1<=5 =>True "HW" i=1+1=2
# i=2   2<=5 =>True "HW" i=2+1=3
# i=3   3<=5 =>True "HW" i=3+1=4
# i=4   4<=5 =>True "HW" i=4+1=5
# i=5   5<=5 =>True "HW" i=5+1=6
# i=6   6<=5 =>False
# .....................................................................
# 1 2 3 4 5 6 7 8 9 10  => 55
# print the sum of numbers from 1 to 10 using while loop

i=1
s=0
while i<=10:
    s+=i
    i+=1

print("sum: ",s)

# Dry run 
# i=1  s=0
# i=1 1<=10 => T s=0+1=1 i=1+1=2
# i=2 2<=10 => T s=1+2=3 i=2+1=3
# i=3 3<=10 => T s=3+3=6 i=3+1=4
# i=4 4<=10 => T s=6+4=10 i=4+1=5
# i=5 5<=10 => T s=10+5=15 i=5+1=6
# i=6 6<=10 => T s=15+6=21 i=6+1=7
# i=7 7<=10 => T s=21+7=28 i=7+1=8
# i=8 8<=10 => T s=28+8=36 i=8+1=9
# i=9 9<=10 => T s=36+9=45 i=9+1=10
# i=10 10<=10=> T s=45=10=55 i=10+1=11
# i=11 11<=10 => F................
# sum: 55
# ........................................................................
# print the product of numbers from 1 to 10 using while loop

# Print all the multiples of 3 from 0 to 40

# i=1
# while i<=40:
#     if i%3==0:
#         print(i)
#     i+=1
# .........................................................................
# Print the average of even numbers from 1 to 100 include both