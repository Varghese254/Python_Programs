#file handling
fo=open("chinmaya.txt","w")
fo.write("programing with python\npython is simple\npython is fun")
fo.close()
print("file",fo.name,"closed")
print("mode of openeing is",fo.mode)
print(fo.closed)
