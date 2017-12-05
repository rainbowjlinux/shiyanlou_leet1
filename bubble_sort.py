# -*- coding: utf-8 -*-

# numlist = [3, 5, 2, 7, 1, 0, 4, 6, 9, 8]
numlist = [3, 2, 1]


def bubble_sort(list):
    print(list)
    for i in range(len(list)):
        for j in range(1, len(list) - i):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
            print(list)

    return list


print(bubble_sort(numlist))
