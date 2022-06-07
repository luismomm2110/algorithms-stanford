from itertools import combinations
from math import sqrt
import numpy as np


def euclidianDistance(k, j, cities):
    return sqrt((np.array(cities[k - 1][0]) - np.array(cities[j - 1][0]))**2 +
                (np.array(cities[k - 1][1]) - np.array(cities[j - 1][1]))**2)


def open_file(path):
    f = open(path)

    numCities = int(f.readline())
    cities = {}
    i = 0

    for line in f.readlines():
        xcoord, ycoord = list(map(float, line.split()))
        cities[i] = [xcoord, ycoord]
        i += 1

    return numCities, cities


def TSP(numCities, cities):
    listSubsets = {}
    i = 0
    for k in range(numCities + 1):
        for subset in combinations(range(2, numCities + 1), k):
            listSubsets[(1, ) + subset] = i
            i += 1
    last = i - 1
    A = {}
    for i in range(len(listSubsets)):
        A[i, 1] = 0 if i == 0 else float('inf')
    for m in range(2, numCities + 1):
        for subset in listSubsets.keys():
            if len(subset) != m:
                continue
            for j in set(subset) - {1}:
                listForMinDistances = []
                for k in set(subset):
                    if k != j:
                        idx = listSubsets[tuple(sorted(set(subset) - {j}))]
                        currentSubset = A[idx, k] + euclidianDistance(
                            k, j, cities)
                        listForMinDistances.append(currentSubset)
                A[listSubsets[subset], j] = min(listForMinDistances)
    finalResults = []
    for j in range(2, numCities + 1):
        finalResults.append(A[31, j] + euclidianDistance(1, j, cities))
    return min(finalResults)


def main():
    num_cities, cities = open_file("tsp_test.txt")

    print(TSP(num_cities, cities))


if __name__ == "__main__":
    main()
