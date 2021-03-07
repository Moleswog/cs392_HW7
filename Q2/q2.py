def by4(x):
    if(x % 4 == 0):
        return True
    else:
        return False

def by100(x):
    if(x % 100 == 0):
        return True
    else:
        return False

def by400(x):
    if(x % 400 == 0):
        return True
    else:
        return False

def leapYear(x):
    if(by400(x) or (by4(x) and (by100(x) == False))):
        print(x, "is a leap year")
        return True
    else:
        print(x, "is not a leap year")
        return False


