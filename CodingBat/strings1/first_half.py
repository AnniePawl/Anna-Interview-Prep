# Given a string of even length, return first half


def first_half(str):
    middle = int(len(str) / 2)
    return str[:middle]


print(first_half("Milk"))  # Mi
print(first_half("crickets"))  # cric
print(first_half("SourPowers"))  # SourP
