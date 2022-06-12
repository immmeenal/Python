list = [x**2 for x in range(5)]
print(list)
list2 = [x**2 for x in range(5) if x**2 % 2 ==0]
print(list2)


list3 = [x for x in range(101) if x%2 !=0]
print(list3)