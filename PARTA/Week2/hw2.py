# PSEUDOCODE
#  1) DIVIDE 2) CONQUER 3) MERGE AND PIGGYBACK NUMBER OF INVERSIONS 
# Declare variable to count inversions
# Split arrays in two until BASE CASE  
# THEN sort the remaining array AND count inversions
# THEN merge... in merge, SORT and count inversions for the following:
# Compare element by element of first and second array and insert in the result
# If the element of the second is copied, then this element is bigger then all remaining
# in 1st, so add this to Count Inversion
def mergeAndSort(entryArray):
	numberInv = 0

	if len(entryArray) > 1:

		firstArray, secondArray = splitInTwo(entryArray)

		numberInv += mergeAndSort(firstArray)
		numberInv += mergeAndSort(secondArray)
		
		numberInv += merge(entryArray, firstArray, secondArray)

	return numberInv

def merge(entryArray, firstArray, secondArray):
	numberInv = 0
	tempArray = 2*len(firstArray)*[0]
	
	i = 0
	j = 0
	k = 0
	endArray = len(firstArray) 	

	while i  < endArray and j < endArray:
		if firstArray[i] <= secondArray[j]:
			tempArray[k] = firstArray[i]
			i += 1
			k += 1
		else:
			tempArray[k] = secondArray[j]
			j += 1	
			k += 1
			numberInv = numberInv + k + 1

	while i < endArray:
		tempArray[k] = firstArray[i]
		i += 1
		k += 1
	while j < endArray:
		tempArray[k] = secondArray[j]
		j += 1
		k += 1
	
	entryArray = populateArray(entryArray, tempArray)	
	 
	return numberInv
            
def populateArray(entryArray, tempArray):
	
	for i in range(len(entryArray)):
		entryArray[i] = tempArray[i]

	return entryArray

def splitInTwo(wholeArray):
	    positionHalfArray = len(wholeArray)//2
	    leftArray = wholeArray[:positionHalfArray]
	    rightArray = wholeArray[positionHalfArray:]

	    return leftArray, rightArray;

def main():
    print("Count Inversions")
	 
    entryArray = [4, 3, 2, 1]
    countInv = mergeAndSort(entryArray)
    print(countInv)

if __name__ == "__main__":
    main()
