#
# Coding challenge part 11
#
# Consider a list in Python which includes prices of all the items in a store.
#
# Build a function to discount the price of all the products by 10%.
#
# Use map to apply the function to all the elements of the list so that all the product prices are discounted.

def discount(price):
    price = price - (price * 10)/100
    return price

product_prices = [100,200,300,400,500]

updated_price = list(map(discount,product_prices))
print(updated_price)