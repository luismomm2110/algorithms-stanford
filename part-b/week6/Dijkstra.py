def fill_graph(textFile, graph):
    f = open(textFile, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split("\t")
        vertex = int(line[0])
        graph[vertex] = []

        for edge in line[1:-1]:
            graph[vertex].append(list(map(lambda x: int(x), edge.split(","))))

    return graph


def find_min_edge(g, computed_distances, vertices_processed_so_far):
    current_index = 1
    min_distance = 100000

    for i in range(len(computed_distances)):

        if not vertices_processed_so_far[i] and computed_distances[i] <= min_distance:
            min_distance = computed_distances[i]
            current_index = i + 1

    return current_index, min_distance


def update_distances(g, computed_distances, processed_vertex, vertices_processed_so_far):
    for edge in g[processed_vertex]:
        vertex = edge[0]
        weight = edge[1] + computed_distances[processed_vertex-1]

        if not vertices_processed_so_far[vertex-1] and weight < computed_distances[vertex-1]:
            computed_distances[vertex -
                               1] = weight

    return computed_distances


def dij_loop(g, vertices_processed_so_far, computed_distances):

    while not all(vertices_processed_so_far):
        processed_vertex, min_distance = find_min_edge(
            g, computed_distances, vertices_processed_so_far)

        vertices_processed_so_far[processed_vertex-1] = True

        computed_distances = update_distances(
            g, computed_distances, processed_vertex, vertices_processed_so_far)

    return computed_distances


def main():
    g = dict()

    g = fill_graph("graph.txt", g)
    v = 1

    vertices_processed_so_far = [False]*len(g.keys())
    computed_distances = [100000]*len(g.keys())

    computed_distances[v-1] = 0

    computed_distances = dij_loop(
        g, vertices_processed_so_far, computed_distances)

    for index in [7, 37, 59, 82, 99, 115, 144, 165, 188, 197]:
        print(computed_distances[index-1], end=",")


if __name__ == "__main__":
    main()
