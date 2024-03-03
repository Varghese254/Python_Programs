#read a sentenece-count the frequencies of each word
text=input("enter a sentenece:")
counts={}
for char in text:
    if char not in counts:
        counts[char]=1
    else:
         counts[char]+=1
for k,v in counts.items():
    print(k,"=",v)
    
