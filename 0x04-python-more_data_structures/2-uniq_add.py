#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    sum_uniq = 0
    if not my_list:
        return 0
    for number in my_list:
        if number not in uniq_list:
            uniq_list.append(number)
    return sum(uniq_list)
