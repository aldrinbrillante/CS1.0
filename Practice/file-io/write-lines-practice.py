'''
Let's practice writing to a file using .writelines()!

.writelines() writes a list of lines to the file. 

Each line must be a string!
'''

# STEP 1: Store file name in a variable
output_file_name = 'output.txt'

# STEP 2: Open the file in write mode ('w')
outfile = open(output_file_name, "w")

# STEP 3: It is American football season. Write list of the football teams stored in teams to the file.

teams = [
"Atlanta Falcons",
"Baltimore Ravens",
"Carolina Panthers",
"Dallas Cowboys",
"Green Bay Packers",
"Kansas City Chiefs",
"Los Angeles Chargers",
"Los Angeles Rams",
"New England Patriots",
"New York Giants",
"New York Jets",
"Oakland Raiders",
"Philadelphia Eagles",
"Pittsburgh Steelers",
"San Francisco 49ers",
]

outfile.writelines(teams)
  
# Note that all of the lines are not one new lines. 

# TODO: To fix this, add a \n character at the end of each string in the list


# STEP 4: Close the file (We will learn about this the next few slides!)
outfile.close()