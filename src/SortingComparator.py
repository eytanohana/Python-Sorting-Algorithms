import matplotlib.pyplot as plt
from numpy.random import normal
from random import randint, seed
from src.Sorting import *
from time import time

def compareAlgorithms(sort1, sort2, num_tests=15, rand_func=normal):
    """
    This function plots the amount of time it takes for two different
    sorting algorithms to run as a function of the size of their input lists.

    :param sort1: The first sorting algorithm
    :param sort2: The Second Sorting algorithm
    :param num_tests: number of sorts to perform for each algorithm
    ":param rand_func: The random number function you want to use
                    (normal(mean, std) or randInt(lower_bound, upper_bound))
    """

    # Create two lists to hold the times it took
    # to sort both lists using each algorithm
    sort1_times = []
    sort2_times = []
    # We create NUM_TESTS lists of random
    # numbers to sort.
    for i in range(num_tests):
        print(f"Test {i+1}...")
        a = []
        b = []
        # In each successive iteration, we double
        # the size of the lists.
        for j in range(2**i):
            a.append(rand_func(0, 100))
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
                  rand_quick_sort : "Random Pivot Quick Sort", median3_quicksort : "Median of 3 Pivot Quick Sort"}


    # plot the graph
    plt.plot([2**i for i in range(num_tests)], sort1_times, color='red', label=algorithms[sort1])
    plt.plot([2**i for i in range(num_tests)], sort2_times, color='blue', label=algorithms[sort2])
    plt.title('Time as a function of list size')
    plt.xlabel('List Size')
    plt.ylabel('Time(ms) to sort')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    seed(time())
    compareAlgorithms(insertion_sort, median3_quicksort, num_tests=10, rand_func=randint)
