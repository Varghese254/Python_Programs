#read list of fruits-return the longest word with ists length
fruits=input("enter some fruits:").split()
lenfruits=[]
for fruit in fruits:
    lenfruits.append((len(fruit),fruit))
lenfruits.sort()
print("longest fruit is",lenfruits[-1][-1],"and its length is",lenfruits[-1][0])
