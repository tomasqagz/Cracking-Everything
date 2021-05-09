def breakingRecords(scores):
    hs = scores[0]
    ls = scores[0]
    hst = 0
    lst = 0
    for i in range(0, len(scores)):
        if scores[i] > hs:
            hs = scores[i]
            hst += 1
        if scores[i] < ls:
            ls = scores[i]
            lst += 1
    return hst, lst
