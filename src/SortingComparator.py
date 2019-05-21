import matplotlib.pyplot as plt
from numpy.random import normal
from src.Sorting import *
from time import time

def compareAlgorithms(sort1, sort2, num_tests=15):
    """
    This function plots the amount of time it takes for two different
    sorting algorithms to run as a function of the size of their input lists.

    :param sort1: The first sorting algorithm
    :param sort2: The Second Sorting algorithm
    """

    # Create two lists to hold the times it took
    # to sort both lists using each algorithm
    sort1_times = []
    sort2_times = []
    # We create NUM_TESTS lists of random
    # numbers to sort.
    for i in range(num_tests):
        print(f"Test {i}...")
        a = []
        b = []
        # In each successive iteration, we double
        # the size of the lists.
        for j in range(2**i):
            a.append(normal(50, 25))
            b.append(a[-1])

        # get the time it takes to
        # sort the list using the first algorithm
        # and add it to the list
        start_time = time() * 1000
        sort1(a)
        end_time = time() * 1000
        sort1_times.append(end_time - start_time)

        # get the time it takes to
        # sort the list using the second algorithm
        # and add it to the list.
        start_time = time() * 1000
        sort2(b)
        end_time = time() * 1000
        sort2_times.append(end_time - start_time)

    # We make a dictionary to hold the names of the algorithms
    # for labeling the graph.
    algorithms = {bubble_sort : "Bubble Sort", selection_sort : "Selection Sort",
                  insertion_sort : "Insertion Sort", merge_sort : "Merge Sort",
                  rand_quick_sort : "Random Pivot Quick Sort"}

    for k,v in algorithms.items():
        if sort1 is k:
            label1 = v
        if sort2 is k:
            label2 = v

    # plot the graph
    plt.plot([2**i for i in range(num_tests)], sort1_times, color='red', label=label1)
    plt.plot([2**i for i in range(num_tests)], sort2_times, color='blue', label=label2)
    plt.xlabel('List Size')
    plt.ylabel('Time (ms) to sort')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    compareAlgorithms(rand_quick_sort, merge_sort)