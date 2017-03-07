# '''1) Return the indices `A1 B1 C1 D1`, so that 
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1 

# 2) If there are more than one solutions, 
#    then return the tuple of values which are lexicographical smallest. 

# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
# S2 : A2 B2 C2 D2

# S1 is lexicographically smaller than S2 iff
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR 
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2'''

def equal(a):
    m = len(a)
    ht = {}
    c = []
    for i in range(len(a)):
        j = i + 1
        while j < m :
            x = a[i] + a[j]
            if x in ht: 
                ind1 = ht[x][0]
                ind2 = ht[x][1]
                if ind1 != i and ind1 != j and ind2 != i and ind2 != j:               
                    b = list(ht[x])
                    b.append(i)
                    b.append(j)

                    if len(c) == 0:
                        c = b
                    else:
                        replace = False
                        for k in range(len(c)):
                            if c[k] < b[k]:
                                break # we got the lexographical order
                            elif c[k] > b[k]:
                                replace = True
                                break
                            
                        if replace:
                            c = b
                #return 1
            else:
                ht[x] = (i,j)
            j += 1
    

   
    return c

def checkIndices(a,b,c,d):

    if a < b and c < d and a < c and b != c and b != d:
        return True


equal([3,4,7,1,2,9,8])
