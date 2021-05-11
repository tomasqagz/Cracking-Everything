arr = []
   for i in range(0, len(grades)):
        rn = 0
        if grades[i] % 5 == 0 or grades[i] < 38:
            arr.append(grades[i])
        elif grades[i] % 5 == 4:
            rn = grades[i]+1
            arr.append(rn)
        elif grades[i] % 5 == 3:
            rn = grades[i]+2
            arr.append(rn)
        else:
            arr.append(grades[i])

    return arr
