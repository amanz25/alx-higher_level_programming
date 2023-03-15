#!/usr/bin/python3
def uniq_add(my_list=[]):
    num_sum = 0
    num_sets = set(my_list)
    for i in num_sets:
        num_sum += i
    return (num_sum)
