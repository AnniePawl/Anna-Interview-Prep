# Given a string, return a new string where first and last cahracters have been exchanged


def front_back(str):
    if len(str) <= 1:  # basecase
        return str
    middle = str[1:-1]
    return str[len(str)-1] + middle + str[0]


print(front_back('glue'))  # eglug
print(front_back('butter'))  # rutteb
print(front_back('shit'))  # this
