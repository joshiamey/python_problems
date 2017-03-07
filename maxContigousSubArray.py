def maxSub(a):
    maxSum = [0 for i in range(len(a))]
    maxSum[0] = a[0]
    maxSoFar = maxSum[0]   

    for i in range(1,len(a)):
        maxSum[i] = maxSum[i-1] + a[i]

        if maxSum[i] < a[i]:
            maxSum[i] = a[i]

        if maxSoFar < maxSum[i]:
            maxSoFar = maxSum[i]

    return maxSoFar    


max = maxSub([-2])

print(max)