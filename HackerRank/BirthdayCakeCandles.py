def birthdayCakeCandles(candles):

    maxnum = candles[0]
    for i in range(0, len(candles)):
        if candles[i] >= maxnum:
            maxnum = candles[i]

    return candles.count(maxnum)
