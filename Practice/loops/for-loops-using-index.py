#TODO: Using a for loop, print out each color from the list called colors.
colors = ["red", "orange", "green", "blue"]



#TODO: Create a list of 4 names.
names = ["A", "B", "C", "D"]
names_length = len(names)
#TODO: Using a for loop, print out each name with " is awesome!" added after each name.
for i in range(names_length):
    print(names[i] + " is awesome")


#TODO: create a list of five integers
integers = [4, 8, 99, 10, 11]
int_length = len(numbers)
sum = 0
#TODO: print the sum of the numbers in the list
for i in range(int_length):
    sum = integers[i] + sum

print(sum)
print(sum / len(integers))
#TODO: After calulcating the sum, calculate the average.