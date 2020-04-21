# Given a string and a non-negative int n, return a larger string that is n copies of original string


def string_times(str, n):
    return str * n


def string_times_v2(str, n):
    result = ""
    for i in range(n):
        result += str
    return result


print(string_times('Hi', 2))  # HiHi
print(string_times('Glad', 3))  # GladGladGlad
print(string_times('Pie', 4))  # PiePiePiePie

print(string_times_v2("Button", 5))  # ButtonButton
