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

    def findParentIndex(self, i):
        if (i-1) % 2 == 0:
            return int(i/2)
        else:
            return int((i-1)/2)
