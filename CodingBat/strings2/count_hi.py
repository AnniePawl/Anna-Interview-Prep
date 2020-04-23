# Return the number of times substring "hi" appears anywhere in given string


def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i:i+2] == "hi":
            count += 1
    return count


print(count_hi("hihihihi"))  # 4
print(count_hi("hi hippo"))  # 2
print(count_hi("lolli"))  # 0
