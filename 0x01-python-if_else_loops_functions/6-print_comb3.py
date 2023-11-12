#!/usr/bin/python3
def print_zero_to_ten():
    token = True
    for num in range(0, 10):
        num = str(num).zfill(2)
        if token:
            print("{}".format(num), end="")
            token = False
        if not token:
            print(", {}".format(num), end="")


def conditions(number):
    if number[0] == number[1]:
        return False
    reversed_num = number[::-1]
    if int(number) > int(reversed_num):
        return False
    return True


def print_comb_2():
    print_zero_to_ten()
    for num in range(10, 100):
        num = str(num)
        if conditions(num):
            print(", {}".format(num), end="")
    print()


print_comb_2()
