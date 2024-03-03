#read a sentenece-count the frequencies of each word
words=input("enter a sentenece:").split()
counts={}
for word in words:
    if word not in counts:
        counts[word]=1
    else:
         counts[word]+=1
for k,v in counts.items():
    print(k,"=",v)
    
