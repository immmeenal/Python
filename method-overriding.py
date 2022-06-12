# class A:
#
#     def fun1(self):
#         print('feature_1 of class A')
#
#     def fun2(self):
#         print('feature_2 of class A')
#
#
# class B(A):
#
#     def fun1(self):
#         print('Modified feature_1 of class A by class B')
#
#     def fun3(self):
#         print('feature_3 of class B')
#
# obj = B()
#
# obj.fun1()


class Animal:
    def Walk(self):
        print('Hello, I am the parent class')

class Dog(Animal):
    def Walk(self):
        print('Hello, I am the child class')
print('The method Walk here is overridden in the code')

r = Dog()
r.Walk()

r = Animal()
r.Walk()