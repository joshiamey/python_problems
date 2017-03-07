def strstr(a,x):

    if len(x) < 1 or len(a) < 1 or len(a) < len(x):
        return -1

    m = len(x) 
    n = len(a)
    i = 0
    j = i + m
    res = -1
    while  j <= n:

        k = i
        b = 0
        while k <= j and b < m and (a[k] == x[b]):
            k += 1
            b += 1

        # if the index used for looping over 2nd string is higher than len of search that means the
        # while loop succeeded
        if b >= m:
            res = i
            break
        
        i += 1
        j = i + m

    return res

print(strstr("b","b"))
    