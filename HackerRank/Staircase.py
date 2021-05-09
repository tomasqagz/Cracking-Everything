def staircase(n):

    stair = "#"
    for i in range(n):
        print(stair.rjust(n,))
        if i < n:
            stair = stair + "#"
