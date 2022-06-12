file = open("demo.txt", 'r')
# do something with the file
#ontent = file.read()
#rint(content)
#content = file.read(10)
#print(content)
content = file.readline()
print(content)
file.close()


