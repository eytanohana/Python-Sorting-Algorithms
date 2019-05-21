import matplotlib.pyplot as plt
from src.Sorting import *
from random import randint
from time import time

NUM_TESTS = 20
T = 600

def compareAlgorithms(sort1, sort2):
    """
    This function plots the amount of time it takes for two different
    sorting algorithms to run as a function of the size of their input lists.

    :param sort1: The first sorting algorithm
    :param sort2: The Second Sorting algorithm
    """
    sort1_times = []
    sort2_times = []
    for i in range(NUM_TESTS):
        print(f"{i}", end=' ')
        a = []
        b = []
        for j in range(2**i):
            a.append(randint(1, 100))
            b.append(a[-1])

        start_time = time() * 1000
        sort1(a)
        end_time = time() * 1000
        sort1_times.append(end_time - start_time)

        start_time = time() * 1000
        sort2(b)
        end_time = time() * 1000
        sort2_times.append(end_time - start_time)


    algorithms = {bubble_sort : "Bubble Sort", selection_sort : "Selection Sort",
                  insertion_sort : "Insertion Sort", merge_sort : "Merge Sort"}

    for k,v in algorithms.items():
        if sort1 is k:
            label1 = v
        if sort2 is k:
            label2 = v

    plt.plot([2**i for i in range(NUM_TESTS)], sort1_times, color='red', label=label1)
    plt.plot([2**i for i in range(NUM_TESTS)], sort2_times, color='blue', label=label2)
    plt.xlabel('List Size')
    plt.ylabel('Time (ms) to sort')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    compareAlgorithms(bubble_sort, merge_sort)




