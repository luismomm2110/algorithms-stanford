class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.insert(len(self.heap), k)

        last_element = self.heap.insert(-1)
        last_index = len(self.heap)

        parent_index = self.heap.findParent(last_index)

    def findParent(self, i):
        if i % 2 == 0:
            return i/2
        else:
            return int(i/2)

    def isConditionRight(self, i):
