#list
list=[1,10,90,3.5,8+3j,"apple",[1,2,3],(100,200)]
list1=[4,57,8]
print(list)
#print(list[0])
print(list+list1)

"""list3=list1.copy()
del list[1]
print(list)"""

#swapping
a,b=10,2
print(a)
print(b)
b,a=a,b
print(a)
print(b)

list.append("mango")
print(list)
print(list.count(10))

list.remove(10)
print(list.index(3.5))

list.extend(list1)

#reverse a array
list.reverse()
print(list1)

#sorting
list.insert(1,"grapes")
print(list)
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

#poping or dleting the elements
num=list1.pop()
print(list1)
num=list.pop(-3)

list.clear()
print(list)



