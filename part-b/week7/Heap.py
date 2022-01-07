class Heap:
    def __init__(self, isMaxHeap=False):
        self.heap = []
        self.isMaxHeap = isMaxHeap

    def insert(self, k):
        if self.isMaxHeap:
            k = -k

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

    def extract_root(self):
        min = self.heap[0]

        self.heap[0] = self.heap.pop()

        index = 0

        children = self.getChildren(index)

        if not children:
            return min

        while (self.heap[index] > sorted(children.values())[0]):
            smaller_child = sorted(children.values())[0]
            new_key = list(children.keys())[list(
                children.values()).index(smaller_child)]

            bigger_value = self.heap[index]
            smaller_value = self.heap[new_key]

            self.heap[index] = smaller_value
            self.heap[new_key] = bigger_value

            children = self.getChildren(new_key)

            if (not children):
                break

            index = new_key

        if (self.isMaxHeap):
            return -min

        return min

    def getChildren(self, i):
        children = {}

        smaller_index = 2*i + 1
        bigger_index = 2*i + 2

        if (smaller_index <= len(self.heap) - 1):
            children[smaller_index] = self.heap[smaller_index]

        if (bigger_index <= len(self.heap) - 1):
            children[bigger_index] = self.heap[bigger_index]

        return children

    def findParentIndex(self, i):
        if (i-1) % 2 == 0:
            return int(i/2)
        else:
            return int((i-1)/2)

    def length(self):
        return len(self.heap)

    def top_value(self):
        if (self.isMaxHeap):
            return -self.heap[0]

        return self.heap[0]
