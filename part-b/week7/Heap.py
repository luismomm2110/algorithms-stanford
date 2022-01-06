class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.insert(len(self.heap), k)
        inserted_index = len(self.heap) - 1

        parent_index = self.findParentIndex(inserted_index)
        parent_value = self.heap[parent_index]

        while (parent_value > k):
            self.heap[parent_index] = k
            self.heap[inserted_index] = parent_value

            inserted_index = parent_index

            parent_index = self.findParentIndex(inserted_index)
            parent_value = self.heap[parent_index]

    def extract_min(self):
        min = self.heap[0]

        self.heap[0] = self.heap[-1]

        index = 0

        left_child = self.heap[1]
        right_child = self.heap[2]

        children = {1: left_child, 2: right_child}

        while (self.heap[index] > sorted(children.values()[0])):
            temp = self.heap[index]
            new_key = children.keys().index(sorted(children.values()[0]))

        return min

    def findParentIndex(self, i):
        if (i-1) % 2 == 0:
            return int(i/2)
        else:
            return int((i-1)/2)
