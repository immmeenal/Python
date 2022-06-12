class teddy:#class
    quantity = 200#attribute
    #constructor
    def __init__(self,name,color):   #self means reference to that perticular obj itself
        self.color = color
        self.name = name
obj1 = teddy("ted","red")
print(obj1.name)
print(obj1.color)

obj2 = teddy("minal","white")
print(obj2.name)
print(obj2.color)



#obj1 = teddy()#object
#print(obj1.quantity)#access to attribute of class with the help of object

#obj2 = teddy()
#print(obj2.quantity)