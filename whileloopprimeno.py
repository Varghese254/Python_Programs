#prime number using while loop
import math
m=int(input("enter M:"))
n=int(input("enterN:"))
i=m
while(i<=n):
    k=int(math.sqrt(i))
    j=2
    while j<=k:
        if i%j==0:break
        j=j+1
        els:print(i)
        i=i+1
           
