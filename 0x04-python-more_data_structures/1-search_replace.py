#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search_replace - searches an element in list and replaces it
    @search: word to search for
    @replace: word to replace with
    return: list
    """
    if not my_list:
        return my_list
    list_cpy = my_list[:]
    index = 0
    for element in list_cpy:
        if element == search:
            list_cpy[index] = replace
            return list_cpy
        index += 1
    return my_list
