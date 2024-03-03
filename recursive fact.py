#recursive function-factorial of no
def fact(x):
    if x==1:return 1
    else:return(x*fact(x-1))
#main prgrms
num=int(input("enter a number:"))
if num>=1:
    print("factorial of",num,"is",fact(num))
