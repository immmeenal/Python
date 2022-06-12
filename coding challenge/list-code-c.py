# Coding challenge part 2.
#
# 1.Create a list of your favorite food items, the list should have minimum 5 elements.
# 2.List out the 3rd element in the list.
# 3.Add additional item to the current list and display the list.
# 4.Insert an element named tacos at the 3rd index position of the list and print out the list elements.


food = ["a","b","c","d","e"]
print(food)
print(food[2])
food.append("f")
print(food)
food.insert(3,"tacos")
print(food)

# Coding challenge part 3

# Task no 1: Using a for-loop and a range function, print "I am a programmer" 5 times.

# Task no 2: Create a function which displays out the square values of numbers from 1 to 9.

for var in range(1,5):
    print("I am a programmer")

def func():
    for var in range(1,10):
        print(var**2)
func()