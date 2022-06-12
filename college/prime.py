x = int(input("Enter number to check prime number: "))

flag = False

if x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            flag = True
            break

if flag:
    print(x, "is not prime")
else:
    print(x, "is prime")
