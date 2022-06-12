print("Enter 10 numbers: ")
no1 = int(input())
no2 = int(input())
no3 = int(input())
no4 = int(input())
no5 = int(input())
no6 = int(input())
no7 = int(input())
no8 = int(input())
no9 = int(input())
no10 = int(input())

if no1 > no2 and no1 > no3 and no1 > no4 and no1 > no5 and no1 > no6 and no1 > no7 and no1 > no8 and no1 > no9 and no1 > no10:
    print("largest no : ", no1)
elif no2 > no3 and no2 > no4 and no2 > no5 and no2 > no6 and no2 > no7 and no2 > no8 and no2 > no9 and no2 > no10:
    print("largest no : ", no2)
elif no3 > no4 and no3 > no5 and no3 > no6 and no3 > no7 and no3 > no8 and no3 > no9 and no3 > no10:
    print("largest no : ", no3)
elif no4 > no5 and no4 > no6 and no4 > no7 and no4 > no8 and no4 > no9 and no4 > no10:
    print("largest no : ", no4)
elif no5 > no6 and no5 > no7 and no5 > no8 and no5 > no9 and no5 > no10:
    print("largest no : ", no5)
elif no6 > no7 and no6 > no8 and no6 > no9 and no6 > no10:
    print("largest no : ", no6)
elif no7 > no8 and no7 > no9 and no7 > no10:
    print("largest no : ", no7)
elif no8 > no9 and no8 > no10:
    print("largest no : ", no8)
elif no9 > no10:
    print("largest no : ", no9)
else:
    print("largest no : ", no10)
