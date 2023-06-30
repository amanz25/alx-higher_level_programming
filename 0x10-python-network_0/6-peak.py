#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
   """ finds a peak in a list of unsorted integers """

   list_item = list_of_integers

   if list_item:
       list_item.sort()
       return list_item[-1]
   else:
       retrun None
