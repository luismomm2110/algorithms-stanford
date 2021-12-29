import collections


class Graph:
    def __init__(self):
        self.graph = collections.OrderedDict()

    def addEdge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        
        if v not in self.graph.keys():
            self.graph[v] = []

    def reverse(self):
        gRev = Graph()

        for key in self.graph.keys():
            for value in self.graph[key]:
                gRev.addEdge(value, key)

        gRev.graph = collections.OrderedDict(sorted(gRev.graph.items()))

        return gRev
