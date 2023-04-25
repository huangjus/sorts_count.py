# Author: Justin Huang
# GitHub username: huangjus
# Date: 4/25/23
# Description: The code has two functions bubble_count and insertion_count that implement bubble and insertion sort
# algorithms and count comparisons and exchanges made during sorting. They take a list as input and return a tuple
# of two integers. Variables track the number of comparisons and exchanges made.

def bubble_count(a_list):
    """
    Sort a list using bubble sort and count the number of comparisons and exchanges made.
    """
    n = len(a_list)
    comparisons = 0
    exchanges = 0
    for i in range(n):
        for k in range(n - i - 1):
            comparisons += 1
            if a_list[k] > a_list[k + 1]:
                exchanges += 1
                a_list[k], a_list[k + 1] = a_list[k + 1], a_list[k]
    return comparisons, exchanges


def insertion_count(a_list):
    """
    Sort a list using insertion sort and count the number of comparisons and exchanges made.
    """
    n = len(a_list)
    comparisons = 0
    exchanges = 0
    for i in range(1, n):
        value = a_list[i]
        pos = i - 1
        while pos >= 0 and a_list[pos] > value:
            comparisons += 1
            exchanges += 1
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        comparisons += 1
        a_list[pos + 1] = value
    return comparisons, exchanges
