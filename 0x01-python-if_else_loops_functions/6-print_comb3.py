#!/usr/bin/python3
def _conditions(num, _list=[]):
    reversed_num = num[::-1]
    if num in _list or reversed_num in _list or num[0] == num[1]:
        return False
    return True
def print_comb():
    used_numbers = []
    token = True
    for n in range(0,100):
        n = str(n).zfill(2)
        if _conditions(n, used_numbers):
            used_numbers.append(n)
            if not token: print(", {}".format(n), end="")
            if token:
                print("{}".format(n), end="")
                token = False
    print()
print_comb()
