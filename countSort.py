#Counting sort algo
import random

def countSort(arr,maxRange):
    countarr = [0] * (maxRange + 1) #stores count of occurence
    sortedarr = [0] * len(arr)

    for i in arr:
        countarr[i] += 1

    for i in range(1,len(countarr)):
        countarr[i] += countarr[i-1]

    for i in range(0,len(arr)):
        pos = countarr[arr[i]]
        sortedarr[pos - 1] = arr[i]
        countarr[arr[i]] -= 1

    return sortedarr


array = [ random.randint(1,20) for i in range(0,21)]

print(countSort(array,max(array)))