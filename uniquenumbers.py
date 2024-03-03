#read a list and eliminates the duplicates and return new list
numbers=input("enter the numbers:").split()
uniquenumbers=[]
print(numbers)
for number in numbers:
    if number not in uniquenumbers:
        uniquenumbers.append(number)
        print(uniquenumbers)
