#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniques = set(my_list)
    nb = 0
    for x in list_uniques:
        nb += 1

    return (nb)
