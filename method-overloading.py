#
# class edpresso:
#     def Hello(self, name=None):
#         if name is not None:
#             print('Hello ' + name)
#         else:
#             print('Hello ')
#
#
#
# obj = edpresso()
#
#
# obj.Hello()
#
# obj.Hello('Minal')


# Function to take multiple arguments
def add(datatype, *args):

    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''


    for x in args:

        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Minal')
