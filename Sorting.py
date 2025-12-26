##############################################################
#                        Bubble Sort                         #
##############################################################
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
            if ls[j] < ls[j-1]:
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
            if left[l] < right[r]:
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
    pivot come before it and all elements greater than it come after (partition step).

    Runs in O(nlogn) on average and O(n^2) in the worst case.
    It's interesting to notice when we compare quicksort with mergesort
    using the normal distribution random number generator quicksort runs more in line with O(nlogn)
    but with the randint function quicksort appears to behave more along the line of O(n^2)

    :param ls: the list to sort
    """
    def _rand_quick_sort(arr, start, end):

        if start >= end:
            return

        # partition the list and get the index of the pivot
        p_index = _partition(arr, start, end)
        if start != p_index:
            # sort the sublist before the partition's index
            _rand_quick_sort(arr, start, p_index - 1)
        if end != p_index:
            # sort the sublist after the partition's index
            _rand_quick_sort(arr, p_index + 1, end)


    _rand_quick_sort(ls, 0, len(ls) - 1)


def _partition(ls, start, end):
    # choose the pivot to be the last element
    pivot = ls[end]
    i = start - 1
    for j in range(start, end):
        # swap any element smaller than the pivot with current pivot index (i+1)
        # and increment i to shift the pivot index over.
        if ls[j] < pivot:
            ls[j], ls[i + 1] = ls[i + 1], ls[j]
            i += 1

    # finally put the pivot at the correct index.
    ls[i + 1], ls[end] = ls[end], ls[i + 1]
    return i + 1


########################################################################################
#                                   Quick Sort median of 3 Pivot                         #
########################################################################################
def median3_quicksort(ls):
    """
    An implementation of the quick sort algorithm in which the pivot is chosen by taking
    the median of three values chosen from the beginning middle and end of the list.

    :param ls: The list to sort.
    """
    def _median3_quicksort(arr, start, end):
        mid = (start + end) // 2
        # get the median of the three values
        median = [arr[start], arr[mid], arr[end]]
        bubble_sort(median)
        pivot = median[1]

        # partition the list and get the index of the pivot.
        p_index = _partition_pivot(arr, start, end, pivot)
        # Sort the sub-list from the start to the pivot
        if start != p_index:
            _median3_quicksort(arr, start, p_index - 1)
        # Sort the sub-list from the pivot till the end.
        if end != p_index:
            _median3_quicksort(arr, p_index + 1, end)


    _median3_quicksort(ls, 0, len(ls) - 1)

# switch the pivot to the end and call the original pivot function
# which takes the end of the list as the pivot.
def _partition_pivot(ls, start, end, pivot):
    for i in range(start, end):
        if ls[i] == pivot:
            ls[i], ls[end] = ls[end], ls[i]
            break
    return _partition(ls, start, end)
