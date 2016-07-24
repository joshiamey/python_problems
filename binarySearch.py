#binarySearch.py
# The list should be sorted

# This one doesnt use slice operator as it takes o(k) , instead indices are passed

def binarySearch(arr,start,end,item):
    if(start >= end):
        return -1
    
    mid = int((start + end)/ 2)

    if arr[mid] == item:
        return mid
    else:
        if item < arr[mid]:
            return binarySearch(arr,start,mid,item)
        else:
            return binarySearch(arr,mid+1,end,item)



list = [1,2,3,4,5]
print(binarySearch(list,0,len(list),4))
