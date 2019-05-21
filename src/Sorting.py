#########################################################################################################
#                                   Bubble Sort                                                         #
#########################################################################################################
def bubble_sort(ls):
    """
    An implementation of the Bubble Sort algorithm with the optimization that if
    it traverses the list once without swapping at all the function ends.
    The algorithm works by constantly "bubbling" the largest value to the ebd of the list
    Runs in O(n^2).

    :param ls: The list to sort
    """
    for j in range(len(ls)-1, 0, -1):
        for i in range(j):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]


#########################################################################################################
#                                   Selection Sort                                                      #
#########################################################################################################


def selection_sort(ls):
    """
    An implementation of the Selection Sort algorithm.
    The algorithm works by finding the minimum in the list and swapping it
    with the 0'th element. Then finding the next minimum and swapping it with the first
    and so on.
    Runs in O(n^2).

    :param ls: The list to sort
    """
    min_index = 0
    for i in range(len(ls)-1):
        minimum = ls[i]
        min_index = i
        for j in range(i+1, len(ls)):
            if ls[j] < minimum:
                minimum = ls[j]
                min_index = j
        ls[i], ls[min_index] = ls[min_index], ls[i]


#########################################################################################################
#                                   Insertion Sort                                                      #
#########################################################################################################


def insertion_sort(ls):
    """
    An implementation of the Insertion Sort algorithm.
    The algorithm works by starting at the beginning of the list
    and bringing smaller elements towards the beginning.
    Runs in O(n^2).

    :param ls: The list to sort
    """
    for i in range(len(ls)):
        for j in range(i, 0, -1):
            if (ls[j] < ls[j-1]):
                ls[j-1], ls[j] = ls[j], ls[j-1]


#########################################################################################################
#                                   Merge Sort                                                         #
#########################################################################################################


def merge_sort(ls):
    """
    An implementation of the Merge Sort algorithm. The algorithm recursively
    divides the array in half and sorts each half and combines the results back together.
    Runs in O(nlogn)

    :param ls: The list to sort
    """
    if len(ls) > 1:
        # find the middle of the list
        # and split it into the left half and the right half
        mid = len(ls) // 2
        left = ls[:mid]
        right = ls[mid:]

        left_len, right_len = len(left), len(right)

        # recursively sort each half
        merge_sort(left)
        merge_sort(right)

        # merge the sorted halves back together
        # start merging up until the length of the shorter list
        l = r = k = 0
        while l < left_len and r < right_len:
            if (left[l] < right[r]):
                ls[k] = left[l]
                l += 1
            else:
                ls[k] = right[r]
                r += 1
            k += 1

        # add in the rest of the longer one at the end of the list
        # it's guaranteed to still be sorted
        while l < left_len:
            ls[k] = left[l]
            l += 1
            k += 1

        while r < right_len:
            ls[k] = right[r]
            r += 1
            k += 1


########################################################################################
#                                   Quick Sort Arbitrary Pivot                         #
########################################################################################
def rand_quick_sort(ls):
    """
    An implementation of the quick sort algorithm in which the pivot
    is an arbitrary value determined by the last element of the list.
    This algorithm works by recursively dividing the list into sublists
    and recursively sorting them. The algorithm chooses an element called
    the pivot and rearranges the sublists such that all elements smaller than the
    pivot come before it and all elements greater than it come after.
    Runs in O(nlogn) on average and O(n^2) in the worst case.

    :param ls: the list to sort
    """
    def rand_quick_sort(ls, start, end):

        if start >= end:
            return

        pivot_index = partition(ls, start, end)
        if start != pivot_index:
            rand_quick_sort(ls, start, pivot_index - 1)
        if end != pivot_index:
            rand_quick_sort(ls, pivot_index + 1, end)

    def partition(ls, start, end):
        pivot = ls[end]
        i = start - 1
        for j in range(start, end):
            if ls[j] < pivot:
                ls[j], ls[i + 1] = ls[i + 1], ls[j]
                i += 1

        ls[i + 1], ls[end] = ls[end], ls[i + 1]
        return i + 1


    rand_quick_sort(ls, 0, len(ls) - 1)