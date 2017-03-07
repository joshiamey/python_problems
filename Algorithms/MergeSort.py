# Sort algorithm mergesort

def mergesort(arr):
   
    if(len(arr) <= 1):
        return

    mid = int(len(arr) / 2)

    lhs = arr[:mid]
    rhs = arr[mid:]

    mergesort(lhs)
    mergesort(rhs)

    i,j,k = 0,0,0
    print("--- before ---")
    print("lhs = ",lhs)
    print("rhs = ",rhs)
    
    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:
            arr[k] = lhs[i]
            i += 1
        else:
            arr[k] = rhs[j]
            j += 1
        k += 1

    while j < len(rhs):
        arr[k] = rhs[j]
        k += 1
        j += 1
    
    while i < len(lhs):
        arr[k] = lhs[i]
        k += 1
        i += 1

    print("--- after ---")
    print("arr = ",arr)
       

arr = [5,3,8,1,2,7,4]

mergesort(arr)

print(arr)

