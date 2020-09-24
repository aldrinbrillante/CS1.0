'''
Let's practice access values from a dictionary!
To access a value, we access it using its key.

'''

# Imagine that a customer places the following order at your empanada shop:

'''
Order:
1 cheese empanada
2 beef empanadas 
'''

menu = {"chicken": 1.99, "beef":1.99, "cheese":1.00, "guava": 2.50}

# TODO: Using the dictionary called menu, access the prices for  
# chicken and beef. Print the prices to terminal. 
chicken_price = menu["chicken"]
print("Chicken price: ", chicken_price)

beef_price = menu["beef"]
print("Beef price: ", beef_price)


# TODO: Calculate the total price of the order and print it.

total = chicken_price + (2* beef_price)
print("Total price: ", total)