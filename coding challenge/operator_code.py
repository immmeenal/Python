#
# Coding challenge part 13
#
# Using the concept of operator overloading in Python, change the behavior of the multiplication
# operator in a way that multiplication operator behaves like an addition operator.

class operator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self, other):#used mul predefine fun and * operator but done addition
        x = self.x+other.x
        y = self.y+other.y
        return operator(x,y)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

obj1 = operator(3,4)
obj2 = operator(2,6)
res = obj1*obj2
print(res)
