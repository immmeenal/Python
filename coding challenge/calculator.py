# Coding challenge part 1.
# Calculator for calculation of simple interest

p = input('Enter value for principle:')
n = input('Enter the no. of years:')
r = input('Enter the rate of interest: ')

p = int(p)
n = int(n)
r = int(r)

si = (p*n*r)/100
print(si)

