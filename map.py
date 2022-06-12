#def fun(x):
 #   return x+2

newlist = [10,20,30,40,50]
#res = list(map(fun,newlist))
res = list(map(lambda x:x+2,newlist))
print(res)