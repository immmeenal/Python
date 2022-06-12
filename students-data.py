#function based way

# def abc():
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     print(name)
#     print(age)
#
# abc()

#oop way
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def get_data(self):
    #     self.name = input("Enter the name of the student : ")
    #     self.age = input("Enter the age of the student: ")

    def get_data(self, name, age):
        self.name = name
        self.age = age

    def put_data(self):
        print(self.name)
        print(self.age)


obj1 = Student("", "")
name = input("Enter the name of student: ")
age = input("Enter the age of the student: ")
obj1.get_data(name, age)
obj1.put_data()
