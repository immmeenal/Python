#list allow duplicate elements in set but sets does not allow duplicate elements
no = {1,2,3,4,5,6,7,8,9}
print(no)
print(5 in no)
no.add(10)
print(no)
no.remove(10)
print(no)

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
print(set_a | set_b)#union
print(set_a & set_b)#intersecton
print(set_a - set_b)#difference