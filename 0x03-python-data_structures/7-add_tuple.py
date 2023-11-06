#!/usr/bin/python3
def pair_tuple(_tuple):
    if not _tuple or len(_tuple) == 0:
        return (0, 0)
    if len(_tuple) == 1:
        return (_tuple[0], 0)
    if len(_tuple) > 2:
        return (_tuple[0], _tuple[1])
    return _tuple


def add(tuple_a, tuple_b):
    first_item = tuple_a[0] + tuple_b[0]
    second_item = tuple_a[1] + tuple_b[1]
    return (first_item, second_item)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = pair_tuple(tuple_a)
    tuple_2 = pair_tuple(tuple_b)
    result = add(tuple_1, tuple_2)
    return result


'''
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
'''
