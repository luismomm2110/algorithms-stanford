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

def computeInv(withInvArray, countSplit):

    if (len(withInvArray == 4)):
        sortBaseCase(withInvArray, countSplit)
    else:     
        firstHalfInv, secondHalfInv = splitInTwo(withInvArray) 
        computeInv(firstHalfInv, count)
        computeInv(secondHalfInv, count)
    
    return countSplit

def sortBaseCase(baseCaseArray, countInv):
    firstArray, secondArray = splitInTwo(baseCaseArray)
    
    if firstArray[0] > firstArray[1]:
        firstArray = [firstArray[0], firstArray[1]]
        countInv = countInv + 1
        
    if secondArray[0] > secondArray[1]:
        secondArray = [secondArray[0], secondArray[1]]
        countInv = countInv + 1

    return firstArray, secondArray, countInv; 

def splitInTwo(wholeArray):
    arrayOfArrays = np.array_split(wholeArray, 2)

    return arrayOfArrays[0], arrayOfArrays[1];

def main()
    print("Count Inversions")
    
    entryArray = np.array([3, 1, 4, 2]])
    countInv = 0
    computeInv(entryArray, countInv)

def __name__ == "__main__":
    main()