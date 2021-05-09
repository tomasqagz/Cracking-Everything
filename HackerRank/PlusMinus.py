def plusMinus(arr):

    positives = 0
    negatives = 0
    zeros = 0

    for x in range(0, len(arr)):
        if arr[x] > 0:
            positives += 1
        elif arr[x] < 0:
            negatives += 1
        else:
            zeros += 1

    print(positives/n)
    print(negatives/n)
    print(zeros/n)
