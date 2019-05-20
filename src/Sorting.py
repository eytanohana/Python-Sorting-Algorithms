


def bubbleSort(ls):
    """
    The Bubble Sort algorithm with the optimization that if
    it traverses the list once without swapping at all the function ends.

    :param ls: The list to sort
    :return: The list sorted
    """
    for j in range(len(ls)-1, 0, -1):
        for i in range(j):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
    return ls

def selectionSort(ls):
    """
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
    return ls

def insertionSort(ls):
    """
    :param ls: The list to sort
    :return: The list sorted
    """





if __name__ == '__main__':
    ls = [5,4,3,23,43,6,23,8,23,2,1]
    print(ls)

    ls = selectionSort(ls)
    print(ls)