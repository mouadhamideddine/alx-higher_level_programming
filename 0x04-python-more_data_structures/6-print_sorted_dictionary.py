#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    sorted_dict = {}
    for sort_key in sorted_keys:
        print("{}: {}".format(sort_key, a_dictionary[sort_key]))
