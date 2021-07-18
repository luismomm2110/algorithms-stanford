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

def countInversions(entryArray):
	tempArray = [0]*len(entryArray)
	return	mergeAndSort(entryArray, tempArray)

def mergeAndSort9(entryArray, tempArray):
    numberInv = 0

    if len(entryArray) > 1:

	firstArray, secondArray = splitInTwo(entryArray)

	numberInv += mergeAndSort(firstArray)
        numberInv += mergeAndSort(secondArray)
	
	numberInv += merge(entryArray, tempArray)

	return numberInv

def merge(entryArray, tempArray)
		    
		while positionFirstArray < len(firstArray) and positionSecondArray < len(secondArray):
		    if firstArray[positionFirstArray] <= secondArray[positionSecondArray]:            
			sortedAndMergedArray[positionSortedAndMergedArray] = firstArray[positionFirstArray]
			positionFirstArray = positionFirstArray + 1
			# no inversion in this case 
		    else:  
			sortedAndMergedArray[positionSortedAndMergedArray] = secondArray[positionSecondArray]
			countInv = len(firstArray) - positionFirstArray
			positionSecondArray = positionSecondArray + 1
		    positionSortedAndMergedArray = positionSortedAndMergedArray + 1

		while positionFirstArray < len(firstArray):
		    sortedAndMergedArray[positionSortedAndMergedArray] = firstArray[positionFirstArray]
		    positionFirstArray = positionFirstArray + 1
		    positionSortedAndMergedArray = positionSortedAndMergedArray + 1

		while positionSecondArray < len(secondArray):
		    sortedAndMergedArray[positionSortedAndMergedArray] = secondArray[positionSecondArray]
		    positionSecondArray = positionSecondArray + 1
		    positionSortedAndMergedArray = positionSortedAndMergedArray + 1

	return numberInv
            
def splitInTwo(wholeArray):
	    positionHalfArray = len(wholeArray)//2
	    leftArray = wholeArray[:positionHalfArray]
	    rightArray = wholeArray[positionHalfArray:]

	    return leftArray, rightArray;

def main():
	    print("Count Inversions")
	 
	    entryArray = np.array([4, 3, 2, 1])
	    countInversions(entryArray)
	    print(countInv)

if __name__ == "__main__":
	    main()
