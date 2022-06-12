#
# Coding challenge part 12
#
# Using the concept of object oriented programming and inheritance, create a super class named Computer,
# which has two sub classes named Desktop and Laptop.
#
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display
# the specifications of the computer.
#
# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them
# for example laptop can have weight as a special specification.
#
# Make sure that the sub classes have their own methods to get and display their special specification.
#
# Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as
# the methods from the own class

class Computer:
    def __init__(self, money, processor):
        self.money = money
        self.processor = processor

    def getspecs(self):
        self.money = input("Enter the price of computer: ")

        self.processor = input("Enter the processor name : ")


    def displayspecs(self):
        print("here is the specs of computer: ")
        print("computer price is : "+self.money+ "Processor is : "+self.processor)


class Desktop(Computer):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def getD(self):
        self.brand = input("Enter the brand of desktop: ")

        self.color = input("Enter the color of desktop : ")


    def displayD(self):
        print(self.brand)
        print(self.color)

class Laptop(Computer):
    def __init__(self, screen , graphics1):
        self.screen = screen
        self.graphics1 = graphics1

    def getL(self):
        self.screen = input("Enter the screen size: ")

        self.graphics1 = input("Enter the graphics of laptop : ")


    def displayL(self):
        print(self.screen)
        print(self.graphics1)

obj1 = Laptop("","")
obj1.getL()
obj1.displayL()
obj1.getspecs()
obj1.displayspecs()
