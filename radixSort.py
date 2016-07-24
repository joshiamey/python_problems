#Radix sort uses count sort internally, the countsort algo
#is applied on each digit from LSD to MSD


def countsort(arr,x):
    countarr = [0] * (10) #stores count of occurence
    sortedarr = [0] * len(arr)

    #(arr[]/dig % 10) gives digit
    for i in arr:
        digit = int((i / x) % 10)
        countarr[digit] += 1

    for i in range(1,len(countarr)):
        countarr[i] += countarr[i-1]

#start filling up the output array by iterating in reverse order over orignal array
    for i in range(0,len(arr)):
        digit = int((arr[-i - 1] / x) % 10)
        pos = countarr[digit]
        sortedarr[pos - 1] = arr[-i - 1]
        countarr[digit] -= 1

    #copy sortedarr in arr
    for i in range(0,len(arr)):
        arr[i] = sortedarr[i]

def radixSort(arr):

    maxNum = max(arr);
    
    n = 1

    while (maxNum / n) > 0:
        #The n is incremented in multiple of 10
        # n =1 , array sorted based on last digit
        # n = 10, array sorted based on 10s and so on
        countsort(arr,n)
        n *= 10



array = [345,987,567,459,255,156,1357]
radixSort(array)

print(array)






    
