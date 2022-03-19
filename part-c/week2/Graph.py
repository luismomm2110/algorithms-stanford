from collections import defaultdict


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    def find(self, parents, node):
        if parents[node] == node:
            return node
        else:
            return self.find(parents, parents[node])

    def union(self, parents, ranks, vertex1, vertex2):
        parent1 = self.find(parents, vertex1)
        parent2 = self.find(parents, vertex2)

        if ranks[parent1] < ranks[parent2]:
            parents[parent1] = parent2
            ranks[parent1] += 1
            return
        if ranks[parent1] > ranks[parent2]:
            parents[parent2] = parent1
            ranks[parent2] += 1
            return

        else:
            parents[parent2] = parent1
            ranks[parent1] += 1
