# Given 2 strings (a, b), return string of form short + long + short, with shorter string on outsides. Strings will not be same length, but may be empty


def combo_string(a, b):
    lenA = len(a)
    lenB = len(b)
    if lenA > lenB:
        return b + a + b
    else:
        return a + b + a

def combo_string_v2(a,b):
    return a+b+a if len(a)<len(b) else b+a+b



print(combo_string("good", "bye"))  # byegoodbye
print(combo_string("Run", "Forest"))  # RunForestRun
print(combo_string("Stop", "Watch"))  # StopWatchStop
print(combo_string("", ""))  # ""

print(combo_string_v2("good", "bye"))
