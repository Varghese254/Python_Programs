#factorail of a number
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorail of",n,"is",fact)
