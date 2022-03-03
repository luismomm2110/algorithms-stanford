from curses import KEY_C1
from functools import reduce
import random


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


def find_edges_by_vertice(edge, vertex):
    return edge[0] == vertex or edge[1] == vertex


def add_edge(vertex_in_tree, edges, vertex):
    vertex_in_tree.extend(list(
        filter(lambda x: find_edges_by_vertice(x, vertex), edges)))


def main():
    V, edges = import_file("edges.txt")

    X = []
    sum_edges = 0

    first_vertex = 1
    X.append(first_vertex)
    vertex_in_tree = list(
        filter(lambda x: find_edges_by_vertice(x, first_vertex), edges))

    while len(X) < V:
        vertex_in_tree.sort(key=lambda x: x[2])

        for edge in vertex_in_tree:
            if edge[0] not in X:
                sum_edges += edge[2]
                X.append(edge[0])
                add_edge(vertex_in_tree, edges, edge[0])
                break
            if edge[1] not in X:
                sum_edges += edge[2]
                X.append(edge[1])
                add_edge(vertex_in_tree, edges, edge[1])
                break

    print(sum_edges)


if __name__ == "__main__":
    main()
