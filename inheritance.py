class Student:#base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def create(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name)
        print(self.age)
        
class Science_stud(Student):# inheritance #derived class/sub class
    def science(self):
        print("This is a science method ...")

obj1 = Science_stud("","")
name = input("Enter the name of student : ")
age = input("Enter the age of student : ")
obj1.create(name,age)
obj1.show()
obj1.science()
