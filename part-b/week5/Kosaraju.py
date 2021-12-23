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
        if not visited_nodes[i]:
            s = i
            FirstDFS(g, i, visited_nodes, finishing_times)

def FirstDFS(g, i, visited_nodes, finishing_times):
    global t
    visited_nodes[i] = True 

    for edge in g.graph[i]:
        if not visited_nodes[edge]:
            FirstDFS(g, edge, visited_nodes, finishing_times)


    t += 1
    finishing_times[i] = t

def SecondDFSLoop(g, visited_nodes, finishing_times, leaders):
    global s

    for i in reversed(sorted(finishing_times)):
        print(i)


def main():
    global t
    global s 
    s = None
    t = 0 

    g = Graph()
    fill_graph("test.txt", g)
    gRev = g.reverse()

    
    visited_nodes = [False for i in range(len(g.graph.keys()))]
    finishing_times = [0 for i in range(len(g.graph.keys()))]

    FirstDFSLoop(gRev, visited_nodes, finishing_times)
    print(finishing_times)

    visited_nodes = [False for i in range(len(g.graph.keys()))]
    leaders = []


    SecondDFSLoop(g, visited_nodes, finishing_times, leaders)

if __name__ == "__main__":
    main()
