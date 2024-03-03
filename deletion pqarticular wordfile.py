#delete those lines that contains a particular word
import os
def fileDel(filename,word):
    fr=open(filename,"r")
    newfile=open("new.txt","w")
    while True:
        line=fr.readline()
        if not line:
            pass
        else:
            newfile.write(line)
    fr.close()
    newfile.close()
    os.remove(filename)
    os.rename("new.txt",filename)
    
#main progrm
filename=input("enter the word filename:")
word=input("enter the word:")
#function calling
fileDEL(filename,word) 
    
