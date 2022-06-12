class addition:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x= self.x + other.x
        y= self.y + other.y
        return addition(x,y)

    def __str__(self):#format the result
        return "({0},{1})".format(self.x,self.y)

obj1 = addition(1,4)
obj2 = addition(3,6)
res = obj1+obj2
print(res)