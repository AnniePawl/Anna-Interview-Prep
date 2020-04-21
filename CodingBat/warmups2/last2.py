# Given a string, return the count of number of times that a substring length 2 appears in string and also as the last 2  characters of the string (don't count end substring).


def last2(str):
    target = str[-2:]
    # print(target)
    count = 0
    for i in range(len(str)):
        if target in str:
            count += 1
    return count


print(last2('hizzhi'))  # 1
print(last2('hihizzhi'))  # 2
print(last2('xxxhixx'))  # 3
