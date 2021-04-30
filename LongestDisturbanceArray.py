# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 2021

@author: Michael Lin
"""


def longestDisturbanceArray(input_list, num):
    """
    Longest disturbance array
    :param input_list: input list
    :param num: length of list
    :return: maximum length of the sub array
    """
    # Sliding window approach
    start, end, sign, max_length = 0, 1, 0, 1
    prev = input_list[start]
    while end < num:
        if input_list[end] == prev:
            start = end - 1
            sign = 0
        elif sign == -1 and input_list[end] > prev:
            if max_length < end - start:
                max_length = end - start
            sign = 1
        elif sign == 1 and input_list[end] < prev:
            if max_length < end - start:
                max_length = end - start
            sign = -1
        else:
            start = end - 1
            if input_list[end] > prev:
                sign = 1
            else:
                sign = -1
        prev = input_list[end]
        end += 1
    if num > 1:
        return max_length + 1
    return max_length


def longestDisturbanceArrayDP(input_list, num):
    """
    Longest disturbance array
    :param input_list: input list
    :param num: length of list
    :return: maximum length of the sub array
    """
    # Dynamic programming implementation
    res = [1] * num
    sign, prev = 0, input_list[0]
    for i in range(1, num):
        if input_list[i] == prev:
            sign = 0
        elif sign == -1 and input_list[i] > prev:
            res[i] = res[i-1] + 1
            sign = 1
        elif sign == 1 and input_list[i] < prev:
            res[i] = res[i-1] + 1
            sign = -1
        else:
            # This needs to be defaulted to 2 since the question computes the number of points not intervals
            res[i] = 2
            if input_list[i] > prev:
                sign = 1
            else:
                sign = -1
        prev = input_list[i]
    return max(res)


def main():
    ultimate_test = [50, 150] * 50000
    print("Sliding window method: ")
    print(longestDisturbanceArray([9, 4, 2, 10, 7, 8, 8, 1, 9], 9))
    print(longestDisturbanceArray([4, 8, 12, 16], 4))
    print(longestDisturbanceArray([100], 1))
    print(longestDisturbanceArray(ultimate_test, 100000))

    print("\nDynamic programming method: ")
    print(longestDisturbanceArrayDP([9, 4, 2, 10, 7, 8, 8, 1, 9], 9))
    print(longestDisturbanceArrayDP([4, 8, 12, 16], 4))
    print(longestDisturbanceArrayDP([100], 1))
    print(longestDisturbanceArrayDP(ultimate_test, 100000))


if __name__ == '__main__':
    main()
