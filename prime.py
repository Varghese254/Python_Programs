#nested for loop
#generate prime numbers b/w 2 limits
import math
m=int(input("enter M:"))
n=int(input("enter N:"))
for i in range(m,n+1):
    k=int(math.sqrt(i))
    for j in range(2,k+1):
        if i%j==0:break
        else:print(i)
        
        
