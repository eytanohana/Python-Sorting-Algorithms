


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


def merge_sort(ls):
    if len(ls) > 1:
        mid = len(ls) // 2
        left = ls[:mid]
        right = ls[mid:]

        merge_sort(left)
        merge_sort(right)








if __name__ == '__main__':
    ls = [6,5,4,3,2,1]
    print(ls)

    merge_sort(ls)
    print(ls)