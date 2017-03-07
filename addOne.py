
def addone(A):
    b = []
    c = A[:]

    if(len(A) > 1):
        c.clear()

        i = 0
        while A[i] <= 0:
            i = i + 1

        while i < len(A):
            c.append(A[i])
            i = i + 1

    add(c,b,len(c)-1,1)

    b.reverse()
    return b

def add(a,b,ind,carryover):

    if ind < 0:
        if carryover != 0:
            b.append(carryover)
        return
    


    tmp = a[ind] + carryover
    print("ind: "+str(ind)+" carryover: "+str(carryover)+" tmp: "+str(tmp))
    if tmp >= 10:
        b.append(0)
        return add(a,b,ind-1,1)
    else:
        b.append(tmp)
        return add(a,b,ind-1,0)


c = addone([0,3,3,5])

for a in c:
    print(a)