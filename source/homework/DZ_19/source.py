def min_nums(number_list):
    min_num = number_list[0]
    for num in number_list:
        if num < min_num:
            min_num = num
    return min_num

def max_nums(number_list):
    max_num = number_list[0]
    for num in number_list:
        if num > max_num:
            max_num = num
    return max_num

def positive_nums(number_list):
    count = 0
    for num in number_list:
        if num > 0:
            count +=1
    return count

def negative_nums(number_list):
    count = 0
    for num in number_list:
        if num < 0:
            count +=1
    return count

def zero_nums(number_list):
    count = 0
    for num in number_list:
        if num == 0:
            count += 1
    return count
