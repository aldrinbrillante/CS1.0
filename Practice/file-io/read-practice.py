'''
Let's practice using .read()!

.read() reads the entire file.

If want it to read a number of characters, pass the number (int) between the parentheses.
'''

# STEP 1: Store file name in a variable
input_file_name = 'languages.txt'

# STEP 2: Open the file in read mode ('r')
infile = open(input_file_name, "r")

# STEP 3: 
# TODO: Using .read() read the first 100 characters of the file and print results

read_data = infile.read(100)
print(read_data)

entire_file = infile.read()
print(entire_file)

# STEP 4: Close the file (We will learn about this the next few slides!)
infile.close()



'''
Now let's practice using .readline()!

.readline() reads one line from the file and returns it. 

The next time you use .readline() again, it will pick up where it left off.
'''

# STEP 1: Store file name in a variable
input_file_name = 'languages.txt'

# STEP 2: Open the file in read mode ('r')
infile = open(input_file_name, "r")

# STEP 3: 

# Using a for loop and .readlines(), we can read and print the first 5 lines of the file.

# line = infile.readline()
# print(line)

for i in range(5):
  line = infile.readline()
  print(line)

# TODO: To avoid double spacing, change the print statement to: print(line, end=' ')

# STEP 4: Close the file (We will learn about this the next few slides!)
infile.close()