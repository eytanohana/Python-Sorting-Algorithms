from time import time

import matplotlib.pyplot as plt
from numpy.random import normal

from Sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, rand_quick_sort, median3_quicksort

# We make a dictionary to hold the names of the algorithms
# for labeling the graph.
algorithms = {
    bubble_sort: 'Bubble Sort',
    selection_sort: 'Selection Sort',
    insertion_sort: 'Insertion Sort',
    merge_sort: 'Merge Sort',
    rand_quick_sort: 'Random Pivot Quick Sort',
    median3_quicksort: 'Median of 3 Pivot Quick Sort',
}


def compare_and_plot_algorithms(sort1, sort2, num_tests=15, rand_func=normal):
    """
    This function plots the amount of time it takes for two different
    sorting algorithms to run as a function of the size of their input lists.

    :param sort1: The first sorting algorithm
    :param sort2: The Second Sorting algorithm
    :param num_tests: number of sorts to perform for each algorithm
    ":param rand_func: The random number function you want to use
                    (normal(mean, std) or randInt(lower_bound, upper_bound))
    """
    print(f'comparing `{algorithms[sort1]}` vs `{algorithms[sort2]}`')
    # Create two lists to hold the times it took
    # to sort both lists using each algorithm
    sort1_times = []
    sort2_times = []
    # We create NUM_TESTS lists of random numbers to sort.
    for i in range(num_tests):
        print('.', end='')
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

    print()
    # plot the graph
    plt.plot([2**i for i in range(num_tests)], sort1_times, '-o', color='red', label=algorithms[sort1])
    plt.plot([2**i for i in range(num_tests)], sort2_times, '-o', color='blue', label=algorithms[sort2])
    plt.title('Time to Sort vs List Size')
    plt.xlabel('List Size')
    plt.ylabel('Time to sort (ms)')
    plt.legend()
    plt.show()
