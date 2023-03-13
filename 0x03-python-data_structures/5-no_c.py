#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i is not 'C' and i is not 'c':
            new_str += i
    return (new_str)
