#loops with condition at the bottom
choice=0
a,b=6,32
while choice!=3:
    print("menu")
    print("1.addition")
    print("2.multiplication")
    print("3.exit")
    choice=int(input("enter ur choice:"))
    if choice==1:print("sum=",a+b)
    if choice==2:print("product=",a*b)
    if choice==3:break
