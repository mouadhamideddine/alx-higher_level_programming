#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace - searches an element in list and replaces it
    @search: word to search for
    @replace: word to replace with
    return: list
    """
    list_cpy = my_list[:]
    index = 0
    for element in list_cpy:
        if element == search:
            list_cpy[index] = replace
        index += 1
    return list_cpy
