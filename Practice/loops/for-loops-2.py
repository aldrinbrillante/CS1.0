#TODO: Using a for loop, print out each color 
# from the list called colors.
colors = ["red", "orange", "green", "blue"]



#TODO: Create a list of 4 names.
names = ["A", "B", "C", "D"]
#TODO: Using a for loop, print out each name with " is awesome!" added after each name.
for name in names:
    print(name + " is awesome")
#TODO: create a list of five integers
numbers = [4, 8, 99, 10, 11]
#TODO: print the sum of the numbers in the list

#create a sum variable
#itirate over the numbers list
#add each number to the sum variable 
sum = 0
for num in numbers:
    sum = sum + num
print(sum)

#TODO: After calulcating the sum, calculate the average.
#average is sum / number of things in the list

average = sum / len(numbers)
print(average) 