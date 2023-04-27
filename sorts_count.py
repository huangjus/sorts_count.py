# Author: Justin Huang
# GitHub username: huangjus
# Date: 4/25/23
# Description: The code has two functions bubble_count and insertion_count that implement bubble and insertion sort
# algorithms and count comparisons and exchanges made during sorting. They take a list as input and return a tuple
# of two integers. Variables track the number of comparisons and exchanges made.

def bubble_count(a_list):
    """
    Sorts a list using Bubble Sort and returns a tuple containing the number of comparisons and exchanges made.
    """
    comparisons = 0
    exchanges = 0
    n = len(a_list)

    for i in range(n - 1):
        for k in range(n - 1 - i):
            comparisons += 1
            if a_list[k] > a_list[k + 1]:
                a_list[k], a_list[k + 1] = a_list[k + 1], a_list[k]
                exchanges += 1

    return comparisons, exchanges


def insertion_count(a_list):
    """
    Sorts a list using Insertion Sort and returns a tuple containing the number of comparisons and exchanges made.
    """
    comparisons = 0
    exchanges = 0
    n = len(a_list)

    for index in range(1, n):
        value = a_list[index]
        pos = index - 1

        while pos >= 0:
            comparisons += 1
            if a_list[pos] > value:
                a_list[pos + 1] = a_list[pos]
                exchanges += 1
                pos -= 1
            else:
                break

        a_list[pos + 1] = value

    return comparisons, exchanges
