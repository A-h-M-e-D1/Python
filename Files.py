# File system and path
# import sys
# my_bath=sys.path
# print(my_bath)

# to deal with path

# path=pathlib.Path("/Users/Dell/Documents/Hello.txt")
# print(pathlib.Path.cwd())

# Relative Windows path
# home=pathlib.Path.home()
# print(home)

# to create a directory
# new_dir=Path.home() / "My_folder"
# files=new_dir / "My_folder" / "file.txt"
 
# Reading and Writing Files
# my_file=Path.open("hello.txt", mode="w")
# my_file.write("Hello and i love python")

# file=open("hello.txt","w")
# file.write("and i love js")

# file=open("hello.txt","r")
# print(file.read())
# print(file.readline())
# print(file.readlines())

# file=open("hello.txt","a")
# file.write("i love science")

# user_input=int(input("Enter Password To open file: "))
# tries=0
# while True:
#     if user_input == 2004:
#         open_file=open("hello.txt",'r')
#         print(open_file.read())
#         break
        
#     else:
#         print("please Enter corrcet password")
#         tries+=1
#     if tries >= 4: # check if tries exceed 4
#         print("You have exceeded the maximum number of attempts.")
#         break
#     user_input = int(input("Enter Password To open file: "))

# طريقه اخري لفتح ملف 
# with open("hello.txt", "r") as f:
#    data = f.read()
#    print(data)

# protect file by using python
# import zipfile

# # create file to protect
# my_file=zipfile.ZipFile("hello.txt",'w')

# # Enter Your password
# my_file.setpassword(b'Ahmed2004')

# my_file.close()

