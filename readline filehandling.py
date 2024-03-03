#file handling reading from a file-readlines-return as a list
#each item in the list will be each line in the filee
#copy a file
file1=input("enter the sourse file:")
file2=input("enter destination file:")
fr=open(file1,"r")
fw=open(file2,"w")
for line in fr.readlines():
        fw.write(line)
fr.close()
fw.close()
print(fr.name,"copied to",fw.name)
