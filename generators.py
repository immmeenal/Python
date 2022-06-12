#generators are also iterables (something which generate itself or something switch could be iterated)
#generators do not allow indexing like list
#but they can be iterated by using for loop
def funn():
    counter = 0
    while counter < 5:
        yield counter
        counter +=1

for x in funn():
    print(x)

def even(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(even(20)))

