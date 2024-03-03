#exception handling-run time errors
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    result=a/b
    print("result=",result)
except ZeroDivisionError:
    print("division by zero occured")
else:
    print("succesful division")
    
