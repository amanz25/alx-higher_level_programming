#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """

    leng = len(list_of_integers)
    count = leng
    half = leng // 2

    if leng == 0:
        return None

    while True:
        count = count // 2
        if (half < leng - 1
                and list_of_integers[half] < list_of_integers[half + 1]):
            if count // 2 == 0:
                count = 2
            half += count // 2
        elif (count > 0 and
                list_of_integers[half] < list_of_integers[half - 1]):
            if count // 2 == 0:
                count = 2
            half -= count // 2
        else:
            return list_of_integers[half]
