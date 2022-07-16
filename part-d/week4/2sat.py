from korasuju import Graph


def open_file(filepath: str):
    clauses = []
    with open(filepath, "r") as f:
        count_variables = int(f.readline())
        for line in f.readlines():
            current_clause = [int(x) for x in line.split()]
            clauses.append(current_clause)
    return count_variables, clauses


def index_from_zero(k):
    return 2*(k-1) if k > 0 else 2*(abs(k)-1)+1


def index_from_zero_list(values):
    return [2*(k-1) if k > 0 else 2*(abs(k)-1)+1 for k in values]


def main():
    count_variables, clauses = open_file("p6.txt")

    g = createGraph(count_variables, clauses)
    print(g.solve2sat())


def createGraph(count_variables, clauses):
    g = Graph(2*count_variables)

    for clause in clauses:
        g.add_edge(-clause[0], clause[1])
        g.add_edge(-clause[1], clause[0])

    sscs = Graph(2*count_variables)

    for key, value in g.graph.items():
        new_key = index_from_zero(key)
        values = index_from_zero_list(value)
        for value in values:
            sscs.add_edge(new_key, value)
    return sscs


if __name__ == "__main__":
    main()
