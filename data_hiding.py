#encapsulation/ data hiding
class Myclass:
    __hiddden = 0#dundars: (--)
    var = 1

    # def show(self):
    #     print(self.var)
    #     print(self.__hiddden)

    def add(self, increment):
        self.__hiddden += increment
        print(self.__hiddden)


obj1 = Myclass()
# print(obj1.__hidden)# cant access becz of data encapsulation ## only can access with the help of methods
print(obj1.var)
obj1.add(5)
