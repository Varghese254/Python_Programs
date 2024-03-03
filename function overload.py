#method  overloading
class Student:
    def __init__(self,name):
        self.name=name
    def displayName(self):
        print("name of the student=",self.name)
class Teacher(Student):
  def __init__(self,name,teach_name):
      Student.__init__(self,name)
      self.teach_name=teach_name
  def displayName(self):
      print("name of the teacher:",self.teach_name)
#main prgrm
name=input("enter name of ther student:")
teach_name=input("enter, the name of teacher")
stud1=Teacher(name,teach_name)
stud1.displayName()
