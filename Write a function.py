def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            if year % 100 == 0:
                leap = True
            else:
                leap = False
        else:
            if year % 100 != 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    
    return leap
