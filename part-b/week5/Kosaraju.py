from Graph import Graph
import collections
from collections import deque
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
    visited_nodes = [False for i in range(len(g.graph.keys()))]
    finishing_times = deque()


    for i in reversed(g.graph.keys()):
        if not visited_nodes[i-1]:
            FirstDFS(g, i)

def FirstDFS(g, i):
    global t, visited_nodes, finishing_times

    visited_nodes[i-1] = True

    for edge in g.graph[i]:
        if not visited_nodes[edge-1]:
            FirstDFS(g, edge)

    finishing_times.append(i)

def SecondDFSLoop(g):
    global scc_size, visited_nodes, finishing_times
    leaders = [] 
    visited_nodes = [False for i in range(len(g.graph.keys()))]


    while finishing_times:
        current_edge = finishing_times.pop()

        if not visited_nodes[current_edge-1]:
            scc_size = 0
            secondDFS(g, current_edge)
            leaders.append(scc_size)
    return leaders


def secondDFS(g, i):
    global s, scc_size, visited_nodes 
    visited_nodes[i-1] = True

    for edge in g.graph[i]:
        if not visited_nodes[edge - 1]:
            secondDFS(g, edge)

    scc_size += 1

def main():
    global t, s, finishing_times,  visited_nodes
    s = None
    t = 0

    g = Graph()

    fill_graph("graph.txt", g)

    gRev = g.reverse()

    FirstDFSLoop(gRev)

    leaders = SecondDFSLoop(g)

    print(sorted(leaders, reverse = True)[0:5])


if __name__ == "__main__":
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at targetmain()
