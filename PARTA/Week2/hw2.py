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

def sort_and_count(baseCaseArray):
    if baseCaseArray[0] > 

def splitInTwo(wholeArray):
    arrayOfArrays = np.array_split(wholeArray, 2)

    return arrayOfArrays[0], arrayOfArrays[1];


def merge_and_count_inv(withInvArray):
    countSplit = 0

    if (len(withInvArray == 2):
        sort_and_count(withInvArray)


    firstHalfInv, secondHalfInv = splitInTwo(withInvArray) 


def main()
    print("Count Inversions")
    
    entryArray = np.array([3, 1, 4, 2]])
    merge_and_count_inv(entryArray)

def __name__ == "__main__":
    main()