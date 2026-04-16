def calculate_mean(num_list):
    sum = 0
    total = 0
    for num in num_list:
        sum += num
        total+= 1
    return sum/total
    
def find_maximum(num_list):
    max = 9999
    for num in num_list:
        if num < max:
            max = num
    return max

def find_minimum(num_list):
    min = 0
    for num in num_list:
        if num > min:
            min = num
    return min