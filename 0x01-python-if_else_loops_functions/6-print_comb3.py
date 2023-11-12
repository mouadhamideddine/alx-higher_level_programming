#!/usr/bin/python3
def conditions(number):
    if number[0] == number[1]:
        return False
    reversed_num = number[::-1]
    if int(number) > int(reversed_num):
        return False
    return True


def print_comb_2():
    token = True
    for num in range(0, 100):
        num = str(num).zfill(2)
        if conditions(num) and not token:
            print(", {}".format(num), end="")
        if conditions(num) and token:
            print("{}".format(num), end="")
            token = False
    print()


print_comb_2()
