from Graph import Graph


def import_file(path):
    f = open(path, "r")

    lines = f.readlines()

    V = lines[0]
    g = Graph(int(V))

    for line in lines[1:]:
        split_line_in_edges(g, line)

    return g


def split_line_in_edges(g, line):
    edge = line.split()
    edge = list(map(int, edge))
    g.add_edge(edge[0] - 1, edge[1] - 1, edge[2])


def clustering(g, objective_clusters):

    num_clusters = g.num_vertices

    g.edges = sorted(g.edges, key=lambda edge: edge[2])

    parents = []
    ranks = []

    for i in range(g.num_vertices):
        parents.append(i)
        ranks.append(0)

    result = []

    for edge in g.edges:

        vertex1 = edge[0]
        vertex2 = edge[1]
        leader1 = g.find(parents, vertex1)
        leader2 = g.find(parents, vertex2)

        if leader1 != leader2:
            if (num_clusters == objective_clusters):
                break

            result.append(edge)
            g.union(parents, ranks, vertex1, vertex2)
            num_clusters -= 1

    return edge


def main():
    g = import_file("clustering1.txt")

    print(clustering(g, 4))


if __name__ == "__main__":
    main()
