#!/usr/bin/python3
for ascii_value in range(97, 123):
    if (ascii_value != 113 and ascii_value != 101):
        print("{}".format(chr(ascii_value)), end="")
