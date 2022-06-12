#it is function used wih lambda  to filter out perticular list
newlist = [1,3,4,2,6,9,7,8]

res = list(filter(lambda x : x % 2 == 0, newlist))
print(res)