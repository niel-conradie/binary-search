import random
import time


def naive_search(list, target):
    """ Verifying each element in the list. """
    for index in range(len(list)):
        if list[index] == target:
            return index
    return -1


def binary_search(list, target, low=None, high=None):
    """ Divide and Conquer algorithm. """
    # Parameter conditions.
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if high < low:
        return -1

    # Calculate middle point.
    mid_point = (low + high) // 2

    if list[mid_point] == target:
        return mid_point
    elif target < list[mid_point]:
        return binary_search(list, target, low, mid_point - 1)
    else:
        return binary_search(list, target, mid_point + 1, high)


def run():
    """ Building sorted list and running naive/binary search. """
    length = 10_000

    # Building a sorted list.
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    # Naive search.
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f"\nNaive search: {(end - start) / length} seconds.")

    # Binary search.
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f"\nBinary search: {(end - start) / length} seconds.")


if __name__ == '__main__':
    run()
