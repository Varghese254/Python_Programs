#exception handling-run time errors-user defined exception:

class Error(Exception):
    pass
class ValueTooSmall(Error):
    pass
class ValueTooBig(Error):
    pass
#main prgrm
while True:
     try:
        age=int(input("enter a no:"))
        if age<0:
           raise ValueToosmall
        elif age>150:
           raise ValueTooBig
         break
    except ValueTooSmall:
        print("the age entered is below zero..")
    except ValueTooBig:
        print("the age is too hight...")
print("age succesfully entered")
