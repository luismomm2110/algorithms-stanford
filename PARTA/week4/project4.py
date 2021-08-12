from graph import Graph
import random as r

# Pseudocode
# while vertices > 2:
    # random_edge = r.randrange(0, size + 1, 1)
    # graph.get(random_edge)
    # generate graph with one less vertex
    # add all edges in the generated vertex
    # remove self loops
    # recurse 

# return vertex
def karge_min_cut(graph):
    while graph.get_num_vertex() > 2:
        vertex1, vertex2 = graph.random_edge()

        graph.contracte_edge(vertex1, vertex2)

    return graph.graph


def main():
    graph = Graph("test.txt")
    print(karge_min_cut(graph))

if __name__ == "__main__":
    main()