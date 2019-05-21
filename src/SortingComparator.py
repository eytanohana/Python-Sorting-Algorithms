import matplotlib.pyplot as plt
from src.Sorting import *
from random import randint
from time import time

NUM_OF_TESTS = 16

def compareAlgorithms(sort1, sort2):
    sort1_times = []
    sort2_times = []
    for i in range(NUM_OF_TESTS):
        a = []
        b = []
        for j in range(2**i):
            a.append(randint(1, 100))
            b.append(a[-1])

        start_time = time() * 1000
        sort1(a)
        end_time = time() * 1000







if __name__ == '__main__':
    list1 = []

    for i in range(10):
        list1.append(randint(1, 100))
    print(list1)

    bubble_sort(list1)
    print(list1)
    print(time()*1000)