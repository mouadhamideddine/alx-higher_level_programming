#!/usr/bin/python3
def uppercase(str):
    str_list = list(str)
    str_index = 0
    for char in str_list:
        ascii_char = ord(char)
        if ascii_char >= 97 and ascii_char <= 122:
            ascii_char -= 32
            str_list[str_index] = chr(ascii_char)
        str_index += 1
    str_list = ''.join(str_list)
    print("{}".format(str_list))


'''
uppercase("best")
uppercase("Best School 98 Battery street")
'''
