def create_knapsack(path):
    f = open(path)

    size, numItens = map(int, f.readline().split())

    itens = []

    for line in f.readlines():
        item = list(map(int, line.split()))
        itens.append(item)

    return size, numItens, itens


def knapsack(C, numItens, itens):
    A = [[None]*(C+1) for _ in range(numItens+1)]

    for k in range(0, C + 1):
        A[0][k] = 0

    for i in range(1, numItens+1):
        for c in range(0, C+1):
            value_current_item = itens[i-1][0]
            size_current_item = itens[i-1][1]
            if size_current_item > c:
                A[i][c] = A[i-1][c]
            else:
                A[i][c] = max(A[i-1][c], A[i-1]
                              [c-size_current_item] + value_current_item)

    return A[i][c]


def main():
    size, numItens, itens = create_knapsack("./p1.txt")
    print(knapsack(size, numItens, itens))


if __name__ == "__main__":
    main()
