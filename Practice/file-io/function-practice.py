'''
Function Practice: 
modify the code you just wrote by 
creating a function called read_candy() 
that takes in the file name as a parameter 
and returns the lines of the file as a list
'''

# STEP 1: Store the name of the file
input_file_name = "candy.txt"

#TODO: open the candy file for read

def read_candy(filename):

  # STEP 2: Open the file
  infile = open(filename, "r")

  # STEP 3: Read the file using .readlines()
  lines = infile.readlines()

  # STEP 4: Close the file
  infile.close()

  # Return lines
  return lines

read_candy("candy.txt")
#TODO: print out all the lines of the candy file