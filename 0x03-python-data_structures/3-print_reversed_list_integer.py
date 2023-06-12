#!/user/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = -1
    while idx > -(len(my_list) + 1):
        elem = my_list[idx]
        print("{:d}".format(elem))
        idx -= 1
