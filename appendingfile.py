#append a file to another file
file1=input("enter file for appending")
file2=input("enter the file to be appended:")
fa=open(file1,"a")
fr=open(file2,"r")
for line in fr.readlines():
    fa.write(lines)
fa.close()
fr.close()
            
