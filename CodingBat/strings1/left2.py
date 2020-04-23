# Given a string, return "rotated left 2" version where first 2 chars are moved to end. String will be at least length 2


def left2(str):
    return str[2:] + str[:2]


print(left2("java"))  # vaja
print(left2("money"))  # neymo
print(left2("hi"))  # hi
