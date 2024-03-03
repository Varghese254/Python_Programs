#object oreinted progrmming
class Student:
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("rollno=",self.rollno)
        print("name=",self.name)
        print("course=",self.course)
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")

#main prgrm
rollno=int(input("enter roll number:"))
name=input("enter name:")
course=input("enter course:")
stud1=Student(rollno,name,course)
stud1.displayStudent()
del stud1
        
