import numpy as np


def create_graph(path):
    f = open(path)

    vertices, numEdges = map(int, f.readline().split())

    edges = {}

    for line in f.readlines():
        source, dest, weight = list(map(int, line.split()))
        edges[source, dest] = weight

    return vertices, numEdges, edges


def allPairs(A, n):
    for v in range(1, n + 1):
        for w in range(1, n + 1):
            print(f'Path from {v} to {w} has cost {A[v][w][n-1]}')


def floydWarshal(n, numEdges, edges):
    A = np.empty((n + 1, n + 1, n + 1))
    for v in range(1, n + 1):
        for w in range(1, n + 1):
            if v == w:
                A[v][w][0] = 0
            elif (v, w) in edges:
                A[v][w][0] = edges.get((v, w))
            else:
                A[v][w][0] = float("inf")

    for k in range(1, n + 1):
        print(k)
        for v in range(1, n + 1):
            for w in range(1, n + 1):
                A[v][w][k] = min(A[v][w][k - 1],
                                 A[v][k][k - 1] + A[k][w][k - 1])

    for v in range(1, n + 1):
        if A[v][v][n] < 0:
            return "negative cycle"

    #allPairs(A, n)

    return A


def main():
    vertices, numEdges, edges = create_graph("./g2.txt")
    print(np.amin(floydWarshal(vertices, numEdges, edges)))


if __name__ == "__main__":
    main()