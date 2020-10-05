# Your boss gives you this piece of code written by your co-worker.
# The code works but it sure is...hard to look at.
# Use your knowledge of code quality to improve the code and make it nicer so it won't hurt anyone else.

# original code: 
# def c(a):
#     b=0
#     for i in a:
#         b+=i
#     return b

# print(c([4,5,2,-3]))

#define function sum() with parameter num_list
def sum(num_list):
    # create variable result have a starting value of 0
    result = 0
    #for loop regarding num_list parameter 
    for n in num_list:
        #updates result to be equal to 'result + n'
        result += n
    #returns result
    return result

print(sum([4,5,2,-3])) # this prints out the sum of whatever is inside the input list