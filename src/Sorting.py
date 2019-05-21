#########################################################################################################
#                                   Bubble Sort                                                         #
#########################################################################################################
def bubble_sort(ls):
    """
    My implementation of the Bubble Sort algorithm with the optimization that if
    it traverses the list once without swapping at all the function ends.
    The algorithm works by constantly "bubbling" the largest value to the ebd of the list
    Runs in O(n^2).

    :param ls: The list to sort
    :return: The list sorted
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
    My implementation of the Selection Sort algorithm.
    The algorithm works by finding the minimum in the list and swapping it
    with the 0'th element. Then finding the next minimum and swapping it with the first
    and so on.
    Runs in O(n^2).

    :param ls: The list to sort
    :return: The list sorted
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
    My implementation of the Insertion Sort algorithm.
    The algorithm works by starting at the beginning of the list
    and bringing smaller elements towards the beginning.
    Runs in O(n^2).

    :param ls: The list to sort
    :return: The list sorted
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
    My implementation of the Merge Sort algorithm. The algorithm recursively
    divides the array in half and sorts each half and combines the results back together.
    Runs in O(nlogn)

    :param ls: The list to sort
    :return: The list sorted
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
