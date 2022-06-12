
class Child:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isStudent(self):
        return False

class Student(Child):
    def isStudent(self):
        return True

std = Child("Suman")
print(std.getName(), std.isStudent())

std = Student("Minal")
print(std.getName(), std.isStudent())