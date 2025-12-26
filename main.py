from SortingComparator import algorithms, compare_and_plot_algorithms
from itertools import combinations


def main():
    algos = list(combinations(algorithms, 2))
    for algo1, algo2 in reversed(algos):
        compare_and_plot_algorithms(algo1, algo2)


if __name__ == '__main__':
    main()
