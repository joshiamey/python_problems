def maxSub(a):
    maxSofar = 0
    max = 0
    endInd = 0
    SubArr = []
    maxSubArr = []

    for i in a:

        if i >= 0:
            max += i
            SubArr.append(i)
        else:
            max = 0   
            del SubArr[:]
        
        
        if maxSofar < max | ((maxSofar == max) & (len(SubArr) > len(maxSubArr))):
            maxSofar = max             
            maxSubArr = SubArr[:]

    return maxSubArr    


max = maxSub([1,2,5,-7,2,3])

print(max)