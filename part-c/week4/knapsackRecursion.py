
from collections import defaultdict
import sys
sys.setrecursionlimit(2500)


def create_knapsack(path):
    f = open(path)

    size, numItens = map(int, f.readline().split())

    v = [0]
    w = [0]

    for line in f.readlines():
        item = list(map(int, line.split()))
        v.append(item[0])
        w.append(item[1])

    return size, numItens, v, w


def knapsack(wt, val, W, n, cache):

    # base conditions
    if n == 0 or W == 0:
        return 0

    if cache[(n, W)] != -1:
        return cache[(n, W)]

    if wt[n-1] <= W:
        cache[(n, W)] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1, cache),
            knapsack(wt, val, W, n-1, cache))
        return cache[(n, W)]
    elif wt[n-1] > W:
        cache[(n, W)] = knapsack(wt, val, W, n-1, cache)
        return cache[(n, W)]


def main():
    size, numItens, v, w = create_knapsack("./p2.txt")
    t = defaultdict(lambda: -1)
    print(knapsack(w, v, size, numItens, t))


if __name__ == "__main__":
    main()
