import matplotlib.pyplot as plt
from src.Sorting import *
from random import randint
from time import time

NUM_OF_TESTS = 13

def compareAlgorithms(sort1, sort2):
    sort1_times = []
    sort2_times = []
    for i in range(NUM_OF_TESTS):
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



    plt.plot([2**i for i in range(NUM_OF_TESTS)], sort1_times, color='red', label="First")
    plt.plot([2**i for i in range(NUM_OF_TESTS)], sort2_times, color='blue', label='Second')
    plt.xlabel('List Size')
    plt.ylabel('Time (ms) to sort')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    compareAlgorithms(bubble_sort, insertion_sort)




