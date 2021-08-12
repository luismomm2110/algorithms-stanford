import random as r

class Graph:
    def __init__(self, graph_file):
        self.graph = {}
        self.edges = 0
        self.vertex_count = 0
        with open(graph_file, "r") as file:
            for path in file:
                numbers = [int(x) for x in path.split() if x!='\n']
                vertex = numbers[0]
                vertex_edges = numbers[1:]
                self.graph[vertex] = vertex_edges
                self.edges+=len(vertex_edges)
                self.vertex_count+=1            
        self.supervertices = {}
        for key in self.graph:
            self.supervertices[key] = [key]

    def contracte_edge(self, v1, v2):
        for i in self.graph[v2]:
            if v1 not in self.graph[i] and i is not v1:
                self.graph[i].append(v1)
            self.graph[v1].append(i)
        self.vertex_count -= 1
        self.__remove_self_loops(v1)
        self.graph.pop(v2)

    def __remove_self_loops(self, v1):
        for i in self.graph[v1]:
            if i == v1:
                self.graph[v1].remove(i)

    def get_num_vertex(self):
        return self.vertex_count
    
    def random_edge(self):
        random_vertex = r.randrange(1, self.get_num_vertex() + 1, 1)
        random_edge = r.choice(self.graph[random_vertex])  
        return random_vertex, random_edge      
