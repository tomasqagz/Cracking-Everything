def timeConversion(s):
    ispm = s.find("A")
    hour = int(s[0]+s[1])

    if ispm == -1 and hour <= 11:
        hour = hour + 12
        return str(hour)+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
    elif ispm != -1 and hour == 12:
        hour = "00"
        return hour+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
    else:
        return s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]
