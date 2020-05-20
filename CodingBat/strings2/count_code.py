# Return number of times that string "code" appears anywhere in given string- except we'll accept any letter for the "d", so "cope" and "cooe" count.


def count_code(str):
    count = 0
    for i in range(len(str)):
        code_substring = str[i:i+4]
        if (code_substring[:2] == "co") and (code_substring[-1] == "e"):
            count += 1
    return count

def count_code2(str):
    return sum(1 for i in range(len(str)-3) if str[i:i+2]  =='co' and str[i+3] == "e")


print(count_code("codecodecode"))  # 3
print(count_code("cozecopecore"))  # 3
print(count_code("clone"))  # 0


print(count_code2("cozecopecore"))  # 3
print(count_code("clone"))  # 0