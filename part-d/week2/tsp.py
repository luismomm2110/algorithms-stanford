from importlib.resources import open_binary
from itertools import combinations
from math import sqrt, ceil
import numpy as np


def euclidianDistance(k, j, cities):
    return sqrt((np.array(cities[k - 1][0]) - np.array(cities[j - 1][0]))**2 +
                (np.array(cities[k - 1][1]) - np.array(cities[j - 1][1]))**2)


def open_file(path):
    cities = []
    with open(path) as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        for line in lines[1:]:
            cities.append((float(line.split()[0]), float(line.split()[1])))

    return cities, n


def createSubsets(numCities):
    listSubsets = {}
    i = 0
    for k in range(numCities + 1):
        for subset in combinations(range(2, numCities + 1), k):
            listSubsets[(1, ) + subset] = i
            i += 1
    return listSubsets


def fillBaseCase(listSubsets):
    A = {}
    for i in range(len(listSubsets)):
        A[i, 1] = 0 if i == 0 else float('inf')
    return A


def computeMinDistances(cities, listSubsets, subset, A, j):
    listForMinDistances = []
    for k in set(subset):
        if k != j:
            index = listSubsets[tuple(sorted(set(subset) - {j}))]
            distanceToKinThisSubSet = A[index, k] + euclidianDistance(
                k, j, cities)
            listForMinDistances.append(distanceToKinThisSubSet)
    A[listSubsets[subset], j] = min(listForMinDistances)


def findFinalResults(numCities, cities, A):
    finalResults = []
    for j in range(2, numCities + 1):
        finalResults.append(A[2**(numCities - 1) - 1, j] +
                            euclidianDistance(1, j, cities))
    return finalResults


def TSP(cities, numCities):
    listSubsets = createSubsets(numCities)
    A = fillBaseCase(listSubsets)
    for m in range(2, numCities + 1):
        for subset in listSubsets.keys():
            if len(subset) != m:
                continue
            for j in set(subset) - {1}:
                computeMinDistances(cities, listSubsets, subset, A, j)
    finalResults = findFinalResults(numCities, cities, A)
    return min(finalResults)


def main():
    citiesTest, numCitiesTest = open_file("tsp_test.txt")
    print(TSP(citiesTest, numCitiesTest))
    cities, numCities = open_file('p1.txt')
    cities1, n1 = cities[:13], 13
    cities2, n2 = cities[11:], 14
    dist1 = TSP(cities1, n1)
    dist2 = TSP(cities2, n2)
    finalDistance = dist1 + dist2 - 2 * euclidianDistance(n1, n2, cities)
    print(int(finalDistance))


if __name__ == "__main__":
    main()
