# FILE HANDLING
# with open("data.txt","r") as f:
#     content=f.read()
#     print(content)

# print("Bye.....")

# .....................................
# File Modes
# r => read only 
# w => write /overwrite
# a => append
# r+ => read and write
# w+ => read and write
# a+ => read and write
# .......................................................

# with open("file.txt","w") as f:
#     f.write("Hi I am File Handling from Python....")

# with open("data.txt","w") as f:
#     f.write(".....")
# .......................................................
# with open("data2.txt","a") as f:
#     f.write("Hi .... User")
# .......................................................
# r+ => read and write  (file creation not possible)

# with open("data2.txt","r+") as f:
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     f.write("Bye...")
#     print(f.tell())
#     print(f.read())
# ..................................................................... 

