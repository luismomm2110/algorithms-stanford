
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

if __name__ == "__main__":
    main()
