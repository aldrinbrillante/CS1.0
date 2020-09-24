'''
Let's practice updating values from dicitionaries.

We use the same [] approach that we used when accessing values.
'''

# Welcome to StockY (a spin off of StockX.com)

# Below is our inventory dicitonary with the number of sneakers we currently sell.

inventory = {'Jordan 1' : 1,
             'Yeezy'    : 8,
             'Air Max'  : 10,
             'SB Dunk'  : 5,
             'Cortez'   : 20 }


# A customer came in to purchase 2 pairs of  SB Dunks
# TODO: Update the inventory of 'SB Dunk'
inventory["SB Dunk"] -= 2
print(inventory["SB Dunk"])

# A customer came in to return a pair of Yeezys
# TODO: Update the inventory of 'Yeezy'
inventory["Yeezy"] += 1
print(inventory["Yeezy"])
