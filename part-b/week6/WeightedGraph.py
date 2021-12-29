class WeightedGraph:
    def __init__(self):
        self.graph = []


    def addEdge(self, u, weightedEdge):
        self.graph[u] = weightedEdge
