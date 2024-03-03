#read list of fruits-return the longest word with ists length
fruits=input("enter some fruits:").split()
lenfruits=[]
for fruit in fruits:
    lenfruits.append((len(fruit),fruit))
lenfruits.sort()
    print(lenfruits)
