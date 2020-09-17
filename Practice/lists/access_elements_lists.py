''''
Welcome to Jess + Joi's Dog Kennel 🦴

We babysit 7 dogs. 1 per day of the week.

For example: 
On Sunday, we dogsit Henry. 🐕‍🦺
On Friday, we dogsit Wuffles. 🐕
'''

# List of dog names 
dogs = ["Henry", "Odin", "Rookie", "Shin", "Jenny", "Wuffles", "Nugget"]

# TODO: Today is Thursday. Print the 5th element of the list called dog to see which dog will be coming into the kennel. 
print(dogs[5])


#TODO: Using negative indexing, print the name of the dog who will be the last to visit the kennel this week. (i.e. last in the list)
print(dogs[-1])

#TODO: Joi and Jess want to split up the work at the kennel.
# Using list slicing, assign Joi dogs from Sunday thru Tuesday,
# and assign Jess dog from Wednesday to Saturday.
# Create variable joi_dogs and jess_dogs to store results. Print results.

joi_dogs = dogs[0:3]
jess_dogs = dogs[3:] #this assigns jess from element 3 to the reamining lists 
print(joi_dogs)
print(jess_dogs) 



num_visits = [2, 3, 5, 6, 4, 1]

#TODO: num_visit stores the numebr of times a dog has visited our kennel.
# Nugget is visiting for the first time, so his number of returning visits is missing from num_visits. 


# what do you think will happend if you tried to access index 6 in the num_visits?
# Try it an see what happens!


# -->     print(num_visits[6]) causes 'index out of range' error