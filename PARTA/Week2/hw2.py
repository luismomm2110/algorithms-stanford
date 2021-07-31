<<<<<<< HEAD
def mergeSort(entryArray, size):
    temp_array = [0]*size
    return _mergeSort(entryArray, temp_array, 0, size-1)
 

 
def _mergeSort(entryArray, temp_array, left, right):
    inv_count = 0
 
    if left < right:
 
        mid = (left + right)//2

        inv_count += _mergeSort(entryArray, temp_array,
                                    left, mid)

 
        inv_count += _mergeSort(entryArray, temp_array,
                                  mid + 1, right)
 
 
        inv_count += merge(entryArray, temp_array, left, mid, right)
    return inv_count
 
def merge(entryArray, temp_array, left, mid, right):
    i = left     
    j = mid + 1 
    k = left    
    inv_count = 0
 
    while i <= mid and j <= right:
 
        if entryArray[i] <= entryArray[j]:
            temp_array[k] = entryArray[i]
            k += 1
            i += 1
        else:
            temp_array[k] = entryArray[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
 
    while i <= mid:
        temp_array[k] = entryArray[i]
        k += 1
        i += 1
 
    while j <= right:
        temp_array[k] = entryArray[j]
        k += 1
        j += 1
 
    for loop_var in range(left, right + 1):
        entryArray[loop_var] = temp_array[loop_var]
         
    return inv_count

def main(): 
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    result = mergeSort(arr, n)
    print("Number of inversions are", result)
=======
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
>>>>>>> project3

if __name__ == "__main__":
    main()
