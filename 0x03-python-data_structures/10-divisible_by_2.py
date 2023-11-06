#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    count = -1
    list_copy = my_list[:]
    for number in list_copy:
        count += 1
        if number % 2 == 0:
            list_copy[count] = True
        else:
            list_copy[count] = False
    return (list_copy)


'''
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i],
          "is" if list_result[i] else "is not"))
    i += 1
'''
