def miniMaxSum(arr):
    maxsum = sum(arr) - min(arr)
    minsum = sum(arr) - max(arr)

    print(minsum, maxsum)
