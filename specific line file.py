#regular exprsion-compile()
import re
fr=open("bpc.txt","r")
lines=fr.readlines()
fr.close()
#search line by line for the line containing "jav"
keyword=re.compile("is")
for line in lines:
    result=keyword.search(line)
    if result:
        print(line)
    
