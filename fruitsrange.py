#read list of fruits-print those friuts longer N
fruits=input("enter some friuts:").split()
n=int(input("enter N:"))
longfruits=[]
for fruit in fruits:
    if len(fruit)>n:
        longfruits.append(fruit)
print("fruits with length greter than",n,"is",longfruits)
