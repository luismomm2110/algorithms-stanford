# PSEUDOCODE
#  1) DIVIDE 2) CONQUER 3) MERGE AND PIGGYBACK NUMBER OF INVERSIONS 
# Declare variable to count inversions
# Split arrays in two until BASE CASE  
# THEN sort the remaining array AND count inversions
# THEN merge... in merge, SORT and count inversions for the following:
# Compare element by element of first and second array and insert in the result
# If the element of the second is copied, then this element is bigger then all remaining
# in 1st, so add this to Count Inversion
import numpy as np

countInv = 0

def computeInv(withInvArray, countSplit):

    if (len(withInvArray == 4)):
        sortBaseCase(withInvArray, countSplit)
    else:     
        firstHalfInv, secondHalfInv = splitInTwo(withInvArray) 
        computeInv(firstHalfInv)
        computeInv(secondHalfInv)
        mergeAndCount(firstHalfInv, secondHalfInv)
    
def mergeAndCount(firstArray, secondArray):
    global countInv
    sortedAndMergedArray = np.empty(2*len(firstArray))
    
    positionFirstArray = 1
    positionSecondArray = 1

    for positionSortedAndMergedArray in len(firstArray):
            if firstArray[positionFirstArray] <= secondArray[positionSecondArray]:            
                sortedAndMergedArray[positionSortedAndMergedArray] = firstArray[positionFirstArray]
                positionFirstArray = positionFirstArray + 1
                # no split in this case 
            else:  
                sortedAndMergedArray[positionSortedAndMergedArray] = secondArray[positionSecondArray]
                countInv = len(firstArray) - positionFirstArray
                positionSecondArray = positionSecondArray + 1

    return sortedAndMergedArray


def sortBaseCase(baseCaseArray):
    firstArray, secondArray = splitInTwo(baseCaseArray)
    global countInv
    
    if firstArray[0] > firstArray[1]:
        firstArray = [firstArray[0], firstArray[1]]
        countInv= countInv + 1
        
    if secondArray[0] > secondArray[1]:
        secondArray = [secondArray[0], secondArray[1]]
        countInv = countInv + 1

    return firstArray, secondArray; 

def splitInTwo(wholeArray):
    arrayOfArrays = np.array_split(wholeArray, 2)

    return arrayOfArrays[0], arrayOfArrays[1];

def main():
    print("Count Inversions")
    
    entryArray = np.array([3, 1, 4, 2]])
    countInv = 0
    computeInv(entryArray, countInv)

if __name__ == "__main__":
    main()