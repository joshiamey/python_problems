def squareRoot(num):
    lo = 1 
    hi = num
    sqrRoot = 0

    if num < 0:
        print("Expected output is Invalid Input : input should be non negativeERR")

    if num == 0 | num == 1:
        return num

    while lo <= hi:
        mid = int((hi+lo)/2)
        x = mid * mid
       
        if x <= num:
            sqrRoot = mid
            lo = mid + 1            
        elif x > num:
            hi = mid - 1


    return sqrRoot

print(squareRoot(8))
        