# Coding challenge part 7
#
# Write Python code which accepts name of a product and in turn returns their respective prices.
# Make sure to use dictionaries to store products and their respective prices.
# The dictionary should include at least 5 elements.

product = {"comb": 30,"laptop":40000,"fan":20000,"ac":40020,"table":2000}
str = input('Enter the name of the product : ')
if(str in product):
    print(product.get(str))
else:
    print('Product not found')


# Coding challenge part 8 for section 6
#
# List out  all the odd numbers from 1 to 100 using lists in Python.

my_list = list(range(1,100))

for x in my_list:
    if x%2 != 0:
        print(x)



