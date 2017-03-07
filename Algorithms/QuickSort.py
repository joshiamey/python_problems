#Quicksort algorithm

def swap(arr,start,end):    
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp

def quicksort(arr,start,end):
    if (start >= end):
        return

    split_point = partition(arr,start,end)

    quicksort(arr,start,split_point-1)
    quicksort(arr,split_point+1,end)

def partition(arr,start,end):

    pivot = int((end+1-start)/2)
    done = False
    while not done:

        while start < end and arr[start] < arr[pivot]:
            start+=1

        while end > start and arr[end] > arr[pivot]:
            end -= 1

        if start >= end :
            done = True
        else:
            swap(arr,start,end)
            start += 1
            end -= 1

    swap(arr,pivot,end)

    return start


arr = [5,3,1,6,2]

quicksort(arr,0,len(arr)-1)

print(arr)
            