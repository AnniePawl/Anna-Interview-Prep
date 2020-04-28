# Given an integer n, return absolute difference between n and 21, except return double absolute difference if n over 21
# abs() used to return distance between 2 nums



def diff21(n):
    if n <= 21:
        return abs(21-n)
    else:
        return abs(21-n)*2


print(diff21(19))  # 2
print(diff21(10))  # 11
print(diff21(21))  # 0
print(diff21(25))  # 8
