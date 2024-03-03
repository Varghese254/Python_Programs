#check the validity of a passwrd
#atleat one lowercase one upper,one digit
#atleat 1 sppcl char
#minimum length 6 and max 16
import re
while  True:
    p=input("enter a password")
    if len(p)<6 or len(p)>16:
        print("invalid password")
    elif not re.search("[a-z]",p):
        print("invalid passwor")
    elif not re.search("[A-Z]",p):
        print("invalid")
    elif not re.search("[$#@]",p):
        print("invalid")
    else:
        print("valid")
        break
    
