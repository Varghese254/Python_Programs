#delete those lines that begins with #
import os
def fileCommentRemove(filename):
        fr=open(filename,"r")
        newfile=open("new.txt","w")
        while True:
           line=fr.readlines()
           if not line:
              break
           elif line.startswith('#'):
              pass
           else:
            newfile.write(line)
        fr.close()
        newfile.close()
        oc.remove(filename)
        os.rename("new.txt",filename)
#main prgrm
filename=input("enter the filename:")
#function calling
fileCommentRemove(filename)
