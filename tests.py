from collections.abc import Callable

import numpy as np
import pytest

from Sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, rand_quick_sort, median3_quicksort

np.random.seed(1)


@pytest.mark.parametrize(
    'sorting_algo',
    [
        pytest.param(bubble_sort, id='bubble_sort'),
        pytest.param(insertion_sort, id='insertion_sort'),
        pytest.param(selection_sort, id='selection_sort'),
        pytest.param(merge_sort, id='merge_sort'),
        pytest.param(rand_quick_sort, id='rand_quick_sort'),
        pytest.param(median3_quicksort, id='median3_quicksort'),
    ],
)
def test_sorting_algorithm(sorting_algo: Callable[[list[int]], [None]]):
    ls = np.random.randint(0, 100, size=100)
    expected = np.sort(ls)
    print(ls)
    sorting_algo(ls)
    assert np.all(ls == expected)
