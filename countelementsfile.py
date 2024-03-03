#count the frequencies of each word in a file
file1=input("enter sourse file:")
fr=open(file1,"r")
wordcount={}
for word in fr.read().split():
    if word not in wordcount:
        wordcount[count]=1
    else:
        wordcount[word]+=1
fr.close()
for k,v in wordcount.items():
    print(k,"=",v)
                    
