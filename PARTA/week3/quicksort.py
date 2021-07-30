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
        return inputArray[start]
    elif choice == PIVOT_FINAL:
        pivot = inputArray[end]
        swapPositions(inputArray, end, start)

        return pivot

def swapPositions(inputArray, pos1, pos2):
    inputArray[pos1], inputArray[pos2] = inputArray[pos2], inputArray[pos1]
    
def main():
    global totalComparisons

    inputArray = [1, 11, 5, 15, 2, 12, 9, 99, 77, 0]
    inputArray = [10, 9, 8, 7]
    quickSort(0, len(inputArray) - 1, inputArray, PIVOT_FINAL)
    print("Sorted array: ", inputArray)
    print(totalComparisons)

if __name__ == "__main__":
    main()