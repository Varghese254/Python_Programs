#delete a sentence from a specified poasistion
def fileposDel(filename,pos):
    with open(filename,"r") as fr:
        list=fr.readlines()
        fr.close()
        del lines[pos]
    with open(filename,"w") as fw:
        fw.writelines(lines)
        fw.close()
           
#main progrm
filename=input("enter the word filename:")
pos=int(input("enter the position:"))
#function calling
fileposDel(filename,pos)
