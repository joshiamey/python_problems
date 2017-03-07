def diff(a,k):

    ht = {}

    for i in range(len(a)):
        ht[a[i]] = i

    for j in range(len(a)):
        x = a[j] + k
        if x in ht and j != ht[x]:
            return 1


    return 0


diff([0],0)
