# Given 2 strings, return True if either string appears at very end of other string, ignoring caps.


def end_other(a, b):
    lenA = len(a)
    lenB = len(b)
    if (a[-lenB:] == b) or (b[-lenA:] == a):
        return True
    else:
        return False


def end_other2(a, b):
    return (a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()))


print(end_other('Hiabc', 'abc'))  # True
print(end_other('cookie', 'ie'))  # True
print(end_other('Ig', 'Igloo'))  # False
print(end_other('loo', 'Igloo'))  # True


print(end_other2('Hiabc', 'abc'))  # True
print(end_other2('Ig', 'Igloo'))  # False
