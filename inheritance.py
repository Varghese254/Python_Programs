#object oreinted progrmming-inheritance
class Student:
    def getStudent(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("rollno=",self.rollno)
        print("name=",self.name)
        print("course=",self.course)
        #single inheritance
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def displayMarks(self):
        print("total marks:",self.marks)

#main prgrm
rollno=int(input("enter roll number:"))
name=input("enter name:")
course=input("enter course:")
stud1=Test()
stud1=getStudent()
stud1.displayStudent()
stud1.getMarks(marks)
stud1.displayMarks()

