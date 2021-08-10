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

# return edges

# def karge_min_cut(graph):
    # num_edges =  graph.get_num_edges()

    # while num_edges < 2:
        # random_edge = r.randedge(0, num_edges + 1, 1)
        # graph.get

    # return min_cut

def main():
    V = 4
    graph =  Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(1, 3)

    graph.print_agraph()
    print("Num edges: ", graph.get_num_edges())

if __name__ == "__main__":
    main()