
#unorderred array search 
def deq_search(array, element):
    position = 0
    found = False
    while position < len(array) and not douns:
        if array[position] == element:
            found = True
        else:
            position += 1
    
    return found 


#sequential search
def ordered_seq_search(array, element):
    position = 0
    found = False
    stopped = False

    while position < len(array) and not found and not stopped:
        if array[position] == element:
            found = True
        
        #finish screen shots. 


#binary iterative
def binary_search(arr,ele):

    #first and last index values
    first = 0
    last = len(arr)-1
    found = False
    while first <= last and not found:
        mid = (first+last)/2
        #match found
        if arr[mid] == ele:
            found = True
        #set new midpoints up or down depending on comparisons
        else: 
            #set down
            if ele < arr[mid]:
                last = mid -1
            #set up
            else:
                first = mid + 1
    
    return found

#recrusive binary function
#where does it break
def rec_bin_search(arr,ele):
    if len(arr) == 0;
        return False
    
    else:
        mid = len(arr)/2
        if arr[mid] == ele:
            return True
        
        else:
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid], ele)
            else:
                return rec_bin_search(arr[mid+1:], ele)

