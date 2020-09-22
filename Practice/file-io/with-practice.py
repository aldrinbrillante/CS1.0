# Solve these problems again, but use the with keyword to close the files

filename = "candy.txt"

# TODO use with to open file
with open(filename, "a") as outfile:
  
  candy_list = ["nerds\n", "ringpop\n", "gummy bears\n"]

  outfile.writelines(candy_list)

#TODO: Open the file in for append. Be sure to create a new "with" statement.
# with open("candy.txt" , "a") as outfile:
#     for candy in candy_list:
#         outfile.write(candy)

#TODO: Add 3 types of candy to the lists