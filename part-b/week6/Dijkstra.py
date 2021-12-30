from os import minor


def fill_graph(textFile, graph):
    f = open(textFile, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split("\t")
        vertex = line[0]
        graph[vertex] = []

        for edge in line[1:-1]:
            graph[vertex].append(list(map(lambda x: int(x), edge.split(","))))

    return graph


def dij_loop(g, vertices_processed_so_far, computed_distances):
    for vertex in g.keys():
        if vertex not in vertices_processed_so_far:
            vertices_processed_so_far.append(vertex)
            for edge in g[vertex]:
                computed_distances[edge[0]-1] = edge[1]


def main():
    g = dict()

    g = fill_graph("graph.txt", g)
    v = 1

    vertices_processed_so_far = []
    computed_distances = [10000]*len(g.keys())
    computed_distances[v-1] = 0

    dij_loop(g, vertices_processed_so_far, computed_distances)
    print(computed_distances[80])


if __name__ == "__main__":
    main()
