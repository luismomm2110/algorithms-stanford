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

    def contracte_edge(self, stay_vertex, removed_vertex):
        for i in self.graph[removed_vertex]:
            if i is not stay_vertex and i in self.graph.keys():
                self.graph[i].append(stay_vertex)
                self.graph[stay_vertex].append(i)
        self.vertex_count -= 1
        self.__delete_old_vertex(removed_vertex)
        self.graph.pop(removed_vertex)

    def remove_self_loops(self, stay_vertex):
        for i in self.graph[stay_vertex]:
            if i == stay_vertex:
                self.graph[stay_vertex].remove(i)

    def get_num_vertex(self):
        return self.vertex_count
    
    def get_final_edges(self):
        self.edges = 0
        for i in self.graph.keys():
            self.edges +=  len(self.graph[i])

        return self.edges

    def get_final_nodes(self):
        return list(self.graph.keys())

    def initial_total_edges(self):
        return self.edges
    
    def random_edge(self):
        random_vertex = r.choice(list(self.graph.keys()))
        random_edge = r.choice(self.graph[random_vertex])  
        return random_vertex, random_edge      

    def __delete_old_vertex(self, old_vertex):
        for key in self.graph.keys():
            if old_vertex in self.graph[key]:
                self.graph[key] = list(filter(lambda a: a != old_vertex, self.graph[key]))
