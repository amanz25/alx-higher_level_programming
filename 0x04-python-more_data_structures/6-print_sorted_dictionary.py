#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    sort_dic = {i: a_dictionary[i] for i in keys}
    for i in sort_dic:
        print(i + ":", sort_dic[i])
