x = int(input("Enter percentage: "))
if x in range(75, 101):
    print("Passed with first class")
elif x in range(60, 75):
    print("Passed with Second class")
elif x in range(50, 60):
    print("Passed with Third class")
elif x in range(40, 50):
    print("Passed with Fourth class")
elif x in range(0, 40):
    print("Failed")
else:
    print("Enter valid percentage")
