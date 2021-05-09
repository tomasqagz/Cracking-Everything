def diagonalDifference(arr):
    fd = 0
    fl = 0
    for x in range(n):
        fd = fd+arr[x][x]
        fl = fl+arr[x][n-1-x]

    return abs(fl-fd)
