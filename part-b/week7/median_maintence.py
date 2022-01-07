from Heap import *


def read_file(textfile):
    stream_values = []

    f = open(textfile, "r")
    lines = f.readlines()

    for line in lines:
        stream_values.append(int(line))

    return stream_values


def calculate_median(max_heap, min_heap):
    if (max_heap.length() == min_heap.length()):
        return (max_heap.top_value() + min_heap.top_value())/2
    elif (max_heap.length() > min_heap.length()):
        return max_heap.top_value()
    elif (max_heap.length() < min_heap.length()):
        return min_heap.top_value()


def main():
    sequence_numbers = read_file("median.txt")

    import pdb
    pdb.set_trace()

    max_heap = Heap(isMaxHeap=True)
    min_heap = Heap()

    current_median = sum_median = 0

    for value in sequence_numbers:
        if value < current_median:
            max_heap.insert(value)
        else:
            min_heap.insert(value)

        if (max_heap.length() - min_heap.length() > 1):
            min_heap.insert(max_heap.extract_root())
        elif (min_heap.length() - max_heap.length() > 1):
            max_heap.insert(min_heap.extract_root())

        current_median = calculate_median(max_heap, min_heap)

        sum_median = sum_median + current_median

    return print(int(sum_median % 10000))


if __name__ == "__main__":
    main()
