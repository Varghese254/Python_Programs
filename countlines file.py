#open a file and count the no of lines in the file
file1=input("enter sourse file:")
fr=open(file1,"r")
"""countlines=0
for line in fr.readlines():
    countlines+=1
print("no of line:",countlines)
fr.close()"""
print("no of lines:",len(fr.readlines()))
fr.close()
