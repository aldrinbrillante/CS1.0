'''
QUIZ 3 QUESTION 3
Create a dictionary called hats that will store the
following key value pairs representing the type of hat
and the number of hats of that type in your closet: 

snapback: 10, beanie: 5, baseballcap: 3
'''

hats = {"snapback": 10, "beanie": 5, "baseballcap": 3}

# You were invited to a costume party and had to buy a weird top hat
# to complete your costume! Add weird top hat as a new key with a value of 1 to your hats dictionary. 

hats["weird top hat"] = 1
#print(hats)

# You just bought a new snapback! Add 1 to the current count for snapback in your hats dictionary. 
hats["snapback"] += 1
#print(hats)

# The party was over months ago and the weird top hat is taking up way too much space in your closet,
# you donate the weird top hat to a thrift store. Delete the weird top hat key and value from your hats dictionary
hats["weird top hat"] -= 1
print(hats)


