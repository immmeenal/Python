file = open("demo.txt", 'w')
file.write("My name is Meenal, I love python")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()