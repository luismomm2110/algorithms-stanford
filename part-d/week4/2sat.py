from korasuju import Graph


def open_file(filepath: str):
    clauses = []
    with open(filepath, "r") as f:
        count_variables = int(f.readline())
        for line in f.readlines():
            clause = tuple(map(lambda x: int(x), line.split()))
            clauses.append(clause)
    return count_variables, clauses


def main():
    count_variables, clauses = open_file("test.txt")

    g = Graph(count_variables)

    for clause in clauses:
        g.add_edge(clause[0], clause[1])

    print(g.graph)


if __name__ == "__main__":
    main()
