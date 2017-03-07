#Requirement of problem:
# Write an efficient algorithm that searches for a value in an m x n matrix.
# with below properties
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.

def matrixSearch(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    lo = 0 
    hi = cols - 1
    r = 0

    while r < rows:

        while lo <= hi:
            mid = int((hi + lo)/2)

            x = matrix[r][mid]

            if x == target:
                return 1
            elif x < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        r += 1
        lo = 0
        hi = cols - 1

    return 0

def searchMatrix(A, B):
    m = len(A)
    if m == 0:
        return 0
    n = len(A[0])
    low = 0
    high = m*n - 1
    while low <= high:
        mid = int((low+high)/2)
        i = int(mid/n)
        j = int((mid-i)/n)
        if A[i][j] == B:
            return 1
        elif A[i][j] < B:
            low = mid + 1
        else:
            high = mid - 1
    return 0

a = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

searchMatrix(a, 3)







