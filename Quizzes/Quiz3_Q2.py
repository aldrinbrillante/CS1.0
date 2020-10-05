''' QUIZ 3 '''

#----------Question 2----------

#You are given this list of strings
sports = ["basketball", "softball", "football", "baseball", "track"]

#1. Write Python code to write all the strings in the sports list to a
# file called sports.txt with each sport string being on its own line in the file.

with open("sports.txt", 'w') as output:
    for row in sports:
        output.write(str(row) + '\n')

# Write Python code to read the sports.txt file and print out each line of the file to the terminal. 


