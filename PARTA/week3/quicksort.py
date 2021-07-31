totalComparisons = 0

PIVOT_FIRST = 1
PIVOT_FINAL = 2
PIVOT_MEDIAN = 3

def quickSort(start, end, inputArray, choice):
    global totalComparisons

    if (start >= end):
        return

    totalComparisons += (end - start)
    
    partitionIndex = partition(start, end, inputArray, choice)

    quickSort(start, partitionIndex-2, inputArray, choice) 
    quickSort(partitionIndex, end, inputArray, choice) 

def partition(start, end, inputArray, choice):
    pivot = choose_pivot(inputArray, start, end, choice)
    j = i = start + 1

    while j <= end:
        if inputArray[j] < pivot:
            swapPositions(inputArray, i, j)
            i += 1
        j += 1

    swapPositions(inputArray, start, i-1)       

    return i

def choose_pivot(inputArray, start, end, choice):
    if choice == PIVOT_FIRST:
        pivot = inputArray[start]
    elif choice == PIVOT_FINAL:
        pivot = inputArray[end]
        swapPositions(inputArray, end, start)
    elif choice == PIVOT_MEDIAN:
        index_median = median_of_threes(inputArray, start, end)
        pivot = inputArray[index_median]
        swapPositions(inputArray, start, index_median)

    return pivot

def median_of_threes(inputArray, start, end):
    middle_index = int((start + end)//2)

    three_elements = [inputArray[start], inputArray[middle_index], inputArray[end]]

    if three_elements[0] > three_elements[1]:
        if three_elements[0] < three_elements[2]:
            index_median = start
        elif three_elements[1] > three_elements[2]:
            index_median = middle_index
        else: 
            index_median = end
    else:
        if three_elements[1] < three_elements[2]:
            index_median = middle_index
        elif three_elements[0] > three_elements[2]: 
            index_median = start
        else: 
            index_median = end

    return index_median

def swapPositions(inputArray, pos1, pos2):
    inputArray[pos1], inputArray[pos2] = inputArray[pos2], inputArray[pos1]

def create_task_list():
    f = open('QuickSort.txt', 'r')
    task_list = []

    for line in f.readlines():
        task_list.append(int(line))
    
    return task_list

def main():
    global totalComparisons

    inputArray = [1,3,5,2,4,6]
    quickSort(0, len(inputArray) - 1, inputArray, PIVOT_MEDIAN)
    print("Sorted array: ", inputArray)
    print(totalComparisons)

    inputArray = create_task_list()
    quickSort(0, len(inputArray) - 1, inputArray, PIVOT_MEDIAN)
    print("Sorted array: ", inputArray)
    print(totalComparisons)

if __name__ == "__main__":
    main()