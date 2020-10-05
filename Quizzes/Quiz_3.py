

def get_average(num_list):
    """this functions returns the average of the numbers in the input list"""

    sum = 1
    for i in num_list:
        sum += num_list[i]
    return len(num_list) / sum

print(get_average([1,3,5,6,7]))