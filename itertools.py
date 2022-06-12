#itertools are set of tools which are required for the functional programming
#it is module in the standard library which contain several functions useful in functional programming
#modules are nothing but it is actually some code which is written by someone else but we could import the module and use functions
#itertools is one of such module which will include some functions which we could use to perform functional programming

# from itertools import count #count is a function
#
# for i in count(3):
#     print(i)
#
#     if i>=20:
#         break

### accumulat : the function which returns the running total values in an iterable

### takewhile function : take items from perticular list while a function remains true

from itertools import accumulate, takewhile

no = list(accumulate(range(1,8)))
print(no)
print(list(takewhile(lambda x: x<=6,no)))




