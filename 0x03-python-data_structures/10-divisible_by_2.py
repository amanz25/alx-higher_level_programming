#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mylist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            mylist[count] = True
        else:
            mylist[count] = False
    return(mylist)
