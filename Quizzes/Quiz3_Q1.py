''' QUIZ 3 '''

#----------QUESTION 1----------

# #create an empty list
# num_list = [] 
# #create variable 'amount' and have an integer input that asks user how many numbers are on their list
# amount = int(input("How many numbers are in the list? : "))

# #define function get_average with num_list as parameter
# def get_average(num_list):
#     """this functions returns the average of the numbers in the input list"""
#     #for loop in range with the int input given in variable 'amount'
#     for i in range(amount):
#         #allows user to list the numbers in their own list, as long as it is within the parameter that they stated for the variable 'amount'
#         numbers = int(input('Enter number and press enter. Keep inputing the numbers in your list until you reach last number:  '))
#         num_list.append(numbers)
#         # let average = the sum of your list divided by the length of it, finding the average of your list. 
#         average = sum(num_list) / len(num_list)
#     #return average
#     return average

# #now, print / call the function get_average() with num_list still being the parameter
# print(get_average(num_list))

def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    sum = 0
    for i in num_list:
        sum += i 
    return sum / len(num_list)

print(get_average([1,3,5,6,7]))