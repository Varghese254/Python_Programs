#read a email and print the server name
#varghe@gmail.com->gmail
str=input("enter the gmail:").split("@")
print(str)
server=str[-1].split(".")
print("server name:",server[0])
