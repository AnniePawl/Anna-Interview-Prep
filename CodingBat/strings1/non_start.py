# Given 2 strings, return their concatenation, except omit first char of each. Strings will be at least length 1


def non_start(a, b):
    return a[1:] + b[1:]


print(non_start('little', 'hug'))  # ittleug
print(non_start('java', 'code'))  # avaode
print(non_start('lhotl', 'java'))  # hotlava
