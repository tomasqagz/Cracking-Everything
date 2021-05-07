def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        return ("Cat A")

    if abs(x-z) > abs(y-z):
        return("Cat B")

    else:
        return ("Mouse C")
