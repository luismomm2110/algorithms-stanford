from Graph import Graph
import collections
import sys
import threading

def fill_graph(textFile, graph):
    f = open(textFile, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split(" ")
        graph.addEdge(int(line[0]), int(line[1]))


def FirstDFSLoop(g):
    global t, finishing_times, visited_nodes

    for i in reversed(g.graph.keys()):
        if not visited_nodes[i-1]:
            FirstDFS(g, i)


def FirstDFS(g, i):
    global t, finishing_times, visited_nodes

    visited_nodes[i-1] = True

    for edge in g.graph[i]:
        if not visited_nodes[edge-1]:
            FirstDFS(g, edge)

    t += 1
    finishing_times[i-1] = t


def SecondDFSLoop(g, leaders):
    global s, visited_nodes, finishing_times

    for i in reversed(sorted(finishing_times)):
        current_edge = list(g.graph.keys()).index(finishing_times.index(i) + 1) + 1

        if not visited_nodes[current_edge-1]:
            s = current_edge
            secondDFS(g, current_edge, visited_nodes, leaders)


def secondDFS(g, i, visited_nodes, leaders):
    global s
    visited_nodes[i-1] = True

    leaders[i-1] = s
    for edge in g.graph[i]:
        if not visited_nodes[edge - 1]:
          return secondDFS(g, edge, visited_nodes, leaders)

def countSCCs(leaders):
    count = collections.Counter(leaders)
    return count


def main():
    global t, s, finishing_times,  visited_nodes
    s = None
    t = 0

    g = Graph()

    fill_graph("graph.txt", g)

    gRev = g.reverse()

    visited_nodes = [False for i in range(len(g.graph.keys()))]
    finishing_times = [0 for i in range(len(g.graph.keys()))]

    FirstDFSLoop(gRev)

    visited_nodes = [False for i in range(len(g.graph.keys()))]
    leaders = [0 for i in range(len(g.graph.keys()))]

    SecondDFSLoop(g, leaders)

    c = countSCCs(leaders)
    print(c)



if __name__ == "__main__":
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at targetmain()
