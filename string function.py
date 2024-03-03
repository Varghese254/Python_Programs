#strings
str="welcome -to- ooty nice- to meet u"
print(str)
print(len(str))
print(str[11])

#for printing last character we have to index it with -1,as shown below
print(str[-1])

#to crop a sentence,we can do it by this
print(str[2:8])

#without knowing the size of the given strng
print(str[4:])
print(str[:12])

#string concatanation
print(str+" moluse")

#string replication
print(str*2)

#check whether the given word starts or end with.
print(str.startswith("welcom",0,30))
print(str.endswith(" moluse",0,-1))

#joining a string with a hyfen,(*,.)anything else.
s=("meet","ing")
print("+".join(s))

#to split each and every word of a string,inside a single quotes
print(str.split())
print(str.split("-"))
