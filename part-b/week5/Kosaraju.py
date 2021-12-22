from Graph import Graph


def fill_graph(textFile, graph):
    f = open(textFile, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split(" ")
        graph.addEdge(int(line[0]), int(line[1]))


def DFSLoop(g):
    t = 0
    visited_nodes = [False for i in range(len(g.graph.keys()))]
    print(visited_nodes)

    for i in reversed(g.graph.keys()):
        print(i)



def main():
    g = Graph()
    fill_graph("test.txt", g)
    print(g.graph)
    gRev = g.reverse()
    print(gRev.graph)
    print("printing keys")
    DFSLoop(gRev)

if __name__ == "__main__":
    main()
