class teddy:
    quantity = 200
    #constructor
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def func(self,color):
        print("This is a method")
        self.color = color

    def func2(self,name):
        print("2nd method")
        self.name = name

obj1 = teddy("ted","red")
print(obj1.name)
print(obj1.color)
print(obj1.quantity)

obj1.func("orange")
print(obj1.name)
print(obj1.color)

obj1.func2("minal")
print(obj1.name)
print(obj1.color)

