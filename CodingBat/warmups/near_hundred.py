# Given an integer n, return True if it is within 10 of 100 or 200.


def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(near_hundred(93))  # True
print(near_hundred(90))  # True
print(near_hundred(193))  # True
print(near_hundred(78))  # False
print(near_hundred(230))  # False
