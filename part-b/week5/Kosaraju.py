from Graph import Graph


def fill_graph(textFile, graph):
    f = open(textFile, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split(" ")
        graph.addEdge(int(line[0]), int(line[1]))


def DFSLoop(graph):
    t = 0


def main():
    g = Graph()
    fill_graph("graph.txt", g)
    print(g.graph)
    gRev = g.reverse()
    print(gRev.graph)


if __name__ == "__main__":
    main()
