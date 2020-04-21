# Given a string, return the count of number of times that a substring length 2 appears in string and also as the last 2  characters of the string (don't count end substring).


def last2(str):
    if len(str) < 2:  # base case
        return 0

    target = str[-2:]  # get last 2 chars
    count = 0  # keep track of how many time each appears
    for i in range(len(str)-2):
        substring = str[i:i+2]
        if substring == target:
            count += 1
    return count


print(last2('hizzhi'))  # 1
print(last2('hihizzhi'))  # 2
print(last2('xxxxhixx'))  # 3
print(last2("x"))  # 0
