# Coding challenge part 5
#
# Write a function which would divide two numbers, design the function in a manner that it
# handles the divide by zero exception.

def func(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("This is divide by zero error")
        return 0
x = float(input("Enter the numerator :  "))
y = float(input("Enter the denomenator : "))
result = func(x,y)
print(result)

# Coding challenge part 6
# 1. Write Python code to open a file named demo.txt and write some random data into it.
#
# 2. Open the file, read the contents and display them as output.
#
# 3. Write python code to add additional text to the existing file on a new line without
# deleting the previous contents.

file = open("demo1.txt", 'w')
file.write("My name is Meenal")
file.close()

file = open("demo1.txt", 'r')
content=file.read(5)
print(content)
file.close()

file = open("demo1.txt", 'a')
file.write("Append Mode")
file.close()




