# Sort algorithm mergesort

def mergesort(arr,start,end):

    if len(arr) > 1:
        mid = int((start + end) / 2)

        lhs = arr[:mid]
        rhs = arr[mid:]

        mergesort(lhs,start,mid)
        mergesort(rhs,mid+1,end)

        i,j,k = 0,0,0

        while i < len(lhs) and j < len(rhs):
            if lhs[i] <= rhs[j]:
                arr[k] = lhs[i]
                i += 1
            else:
                arr[k] = rhs[j]
                j += 1
            k += 1


arr = [5,3,1,2]

mergesort(arr,0,len(arr))

print(arr)

