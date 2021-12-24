from Graph import Graph


def fill_graph(textFile, graph):
    f = open(textFile, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split(" ")
        graph.addEdge(int(line[0]), int(line[1]))


def FirstDFSLoop(g, visited_nodes, finishing_times):
    global t

    for i in reversed(g.graph.keys()):
        if not visited_nodes[i-1]:
            FirstDFS(g, i, visited_nodes, finishing_times)


def FirstDFS(g, i, visited_nodes, finishing_times):
    global t
    visited_nodes[i-1] = True

    for edge in g.graph[i]:
        if not visited_nodes[edge-1]:
            FirstDFS(g, edge, visited_nodes, finishing_times)

    t += 1
    finishing_times[i-1] = t


def SecondDFSLoop(g, visited_nodes, finishing_times, leaders):
    global s

    for i in reversed(sorted(finishing_times)):
        current_edge = list(g.graph.keys()).index(i)
        if not visited_nodes[current_edge]:
            s = current_edge
            secondDFS(g, current_edge, visited_nodes, leaders)


def secondDFS(g, i, visited_nodes, leaders):
    global s
    visited_nodes[i-1] = True

    leaders[i-1] = s
    for edge in g.graph[i]:
        if not visited_nodes[edge - 1]:
            secondDFS(g, edge, visited_nodes, leaders)


def main():
    global t
    global s
    s = None
    t = 0

    g = Graph()

    fill_graph("test.txt", g)
    print("Graph :  " + str(g.graph))

    gRev = g.reverse()
    print("Graph reverse:" + str(gRev.graph))

    visited_nodes = [False for i in range(len(g.graph.keys()))]
    finishing_times = [0 for i in range(len(g.graph.keys()))]

    FirstDFSLoop(gRev, visited_nodes, finishing_times)
    print("Finishing times: " + str(finishing_times))

    visited_nodes = [False for i in range(len(g.graph.keys()))]
    leaders = [0 for i in range(len(g.graph.keys()))]

    SecondDFSLoop(g, visited_nodes, finishing_times, leaders)
    print("Leaders : " + str(leaders))


if __name__ == "__main__":
    main()
