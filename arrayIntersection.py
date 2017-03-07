def intersection(a,b):

    i = len(a) - 1
    j = len(b) - 1

    out = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            out.append(a[i])
            i += 1
            j += 1
    
    return out

def union(a,b):
    
    i = len(a) - 1
    j = len(b) - 1

    out = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        elif a[i] > b[j]:
            out.append(b[j])
            j += 1
        else:
            out.append(a[i])
            i += 1
            j += 1

    while i < len(a):
        out.append(a[i])
        i += 1
    
    while j < len(b):
        out.append(b[j])
        j += 1
    
    return out


intersection([3,3,4,5,5,6,7,8,8,8,8,9],[1,2,3,3,4,5])
union([1,3,4,5,7],[2,3,5,6])

        