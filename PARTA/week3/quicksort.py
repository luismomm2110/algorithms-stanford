totalComparisons = 0

def quickSort(start, end, inputArray):
    global totalComparisons

    if (start < end):
        totalComparisons += (end - start)
        
        partitionIndex = partition(start, end, inputArray)

        quickSort(start, partitionIndex - 2, inputArray) 
        quickSort(partitionIndex, end, inputArray) 

def partition(start, end, inputArray):
    pivot = inputArray[start]
    j = i = start + 1

    while j < end:
        if inputArray[j] < pivot:
            inputArray = swapPositions(inputArray, i, j)
            i += 1
        j += 1

    # import pdb; pdb.set_trace()
    inputArray = swapPositions(inputArray, start, i-1)       

    return i

def swapPositions(inputArray, pos1, pos2):
    inputArray[pos1], inputArray[pos2] = inputArray[pos2], inputArray[pos1]
    
    return inputArray

def main():
    global totalComparisons

    inputArray = [1, 11, 5, 15, 2, 12, 9, 99, 77, 0]
    inputArray = [1,3,5,2,4,6]
    quickSort(0, len(inputArray) - 1, inputArray)
    print("Sorted array: ", inputArray)
    print(totalComparisons)

if __name__ == "__main__":
    main()