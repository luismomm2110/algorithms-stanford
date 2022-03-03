def import_file(path):
    f = open(path, "r")

    lines = f.readlines()

    V, E = lines[0].split()

    edges = []

    for line in lines[1:]:
        edge = line.split()
        edge = list(map(int, edge))
        edges.append(edge)

    edges.sort(key=lambda x: x[2])

    return int(V), edges


def clustering(num_clusters, edges):
