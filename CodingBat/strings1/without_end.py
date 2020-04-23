#  Given a string, return a version without first and last chars


def without_end(str):
    return str[1:-1]


print(without_end("peanut"))  # eanu
print(without_end("emu"))  # mu
