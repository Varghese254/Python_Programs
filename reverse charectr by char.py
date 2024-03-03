#read a name.reverse it character by char
names=input("enter the name:")
for i in range(len(names)-1,-1,-1):print(names[i],end=" ")
print(names[::-1])

