# Parameter weekday is True if its a weekday, parameter vacation True is its vacation. We sleep in if it is not a weekday or we are on vacation. Return True if we sleep in

# Solution 1


def sleep_in(weekday, vacation):
    if weekday == False:
        return True
    elif vacation == True:
        return True
    else:
        return False

# Shorthand Solution


def sleep_in2(weekday, vacation):
    return(not weekday or vacation)


print(sleep_in(False, False))  # True
print(sleep_in(True, False))  # False
print(sleep_in(False, True))  # True
