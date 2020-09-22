'''
Before Sunday Night Football, you want to go shopping for your favorite snacks! 

Let's create a shopping list with your favorite snacks to eat!
'''

#TODO: create a list of strings containing your favorite snacks
snack_list = ["chips" , "chocolate" , "raisins"]

#TODO: open a new file called "shopping_list.txt" for write
my_list = "shopping_list.txt"
outfile = open(my_list, "w")


#TODO: finish this loop to write your favorite snacks to the shopping_list.txt file
for snack in snack_list:
  outfile.write(snack)



# Notice how the above code overwrites the data with each loop. Let's modify our code to write multiple lines of code to the file!



'''
TODO: 

1. Creating a function called write_shopping_list() that has one parameter called snacks. This function takes a list of strings.

2. You function should write to the file using .writelines() 

'''

def write_shopping_list(snack_list):
    outfile = open("shopping_list.txt" , "w")
    outfile.writelines(snack_list)
    outfile.close()

write_shopping_list(snack_list)


