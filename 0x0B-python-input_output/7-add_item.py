#!/usr/bin/python3
"""  Load, add, save module """
import sys
import json
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """
    load add save
    """
    previous_list = []
    if os.path.exists('add_item.json'):
        previous_list = load_from_json_file('add_item.json')
    previous_list += sys.argv[1:]
    save_to_json_file(previous_list, 'add_item.json')


if __name__ == "__main__":
    main()
