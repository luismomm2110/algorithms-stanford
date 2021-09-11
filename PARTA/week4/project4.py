from graph import Graph
import random as r
from copy import deepcopy

def karge_min_cut(entry_graph):
    while entry_graph.get_num_vertex() > 2:
        vertex1, vertex2 = entry_graph.random_edge()

        entry_graph.contracte_edge(vertex1, vertex2)
        entry_graph.remove_self_loops(vertex1)

    return entry_graph

def main():
    graph = Graph("karge.txt")
    min_edges = graph.initial_total_edges()

    for i in range(len(graph.graph.keys())):
        temp = deepcopy(graph)
        final_graph = karge_min_cut(temp)
        if final_graph.get_final_edges() <= min_edges:
            min_edges = final_graph.get_final_edges()
            final_vertices = final_graph.get_final_nodes()
    
    print("Total edges are: {}".format(min_edges))
    print("Final nodes are: {}, {}".format(final_vertices[0], final_vertices[1]))

if __name__ == "__main__":
    main()
