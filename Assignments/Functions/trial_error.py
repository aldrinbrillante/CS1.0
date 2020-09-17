def area(width, height):
    result = width * height
    return result

result_1 = area(5, 6)
print(result_1)

# Q3 Task: Add two more calls to the area() function to your functions.py file
result_2 = area(12, 12)
result_3 = area(11, 11)

print(result_2)
print(result_3)

# Q4 Task: In your functions.py file, fill in the blanks and complete the subtract() function
# ___ subtract(num1, num2):
#    ___ = num1 - num2
#    ___ result

def subtract(num1, num2):
    result = num1 - num2
    return result

# Q5 Task: Add two calls to your completed subtract() function in your functions.py file and print out the results.
result_4 = subtract(20, 10)
result_5 = subtract(100, 50)
print(result_4)
print(result_5)

# Q6: Consider this description:
# "Write a function called divide() which takes in two numbers and returns the first number divided by the second number"

# To write this function definition we first need to identify what the inputs
# or parameters are and then what the output should be or what the function should return.

def divide(dividend, divisor):
    quotient = (dividend / divisor)
    return quotient

quotient = divide(50, 10)
print(quotient)

# Q7 Task: Write the function definition for add() in to the functions.py file
# and then call add() twice with some different values and print() the results.
# "Write a function called add which takes in two numbers and returns the numbers summed together"

def add(number1, number2):
    sum = number1 + number2
    return sum

sum_1 = add(100, 50)
sum_2 = add(25, 25.5)

print(sum_1)
print(sum_2)