#!/usr/bin/python3
def no_c(my_string):
    s = my_string.translate({ord(i): None for i in 'cC'})
    return s
