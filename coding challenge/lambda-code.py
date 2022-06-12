# Coding challenge part 10 for section 8
#
# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.

res = (lambda x: x*(x+5)^2)(5)
print(res)