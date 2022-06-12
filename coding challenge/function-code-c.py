# Coding challenge part 4
#
# Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
#
#  BMI = (weight in Kg)/(Height in Meters)^2.
#
# Write python code which can accept the weight and height of a person and calculate his BMI.
#
# note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

def func(w,h):
    return w/(pow(h,2))

# BMI = func(58,5.4)
# print(BMI)

w = float(input("Enter weight: "))
h = float(input("Enter height: "))
BMI = func(w,h)
print(BMI)