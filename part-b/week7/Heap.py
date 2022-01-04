class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.insert(len(self.heap), k)
        inserted_index = len(self.heap)

        import pdb
        pdb.set_trace()

        parent_index = self.findParentIndex(inserted_index) - 1
        parent_value = self.heap[parent_index]

        while (not self.isConditionRight(inserted_index)):
            self.heap[parent_index] = k
            self.heap[inserted_index] = parent_value

            inserted_index = parent_index + 1

            parent_index = self.findParentIndex(inserted_index) - 1
            parent_value = self.heap[parent_index]

    def findParentIndex(self, i):
        if i % 2 == 0:
            return int(i/2)
        else:
            return int(i/2)

    def isConditionRight(self, i):
        if i % 2 == 0:
            return (self.heap[self.findParentIndex(i) - 1] > self.heap[i-1])
        else:
            return (self.heap[self.findParentIndex(i) - 1] < self.heap[i-1])
