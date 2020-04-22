# Given 2 strings, a and b, return result of putting them togeher in the order abba.


def make_abba(a, b):
    return a + b + b + a


print(make_abba("Hello", "Bye"))  # HelloByeByeHello
print(make_abba("Milk", "Egg"))  # MilkEggEggMilk
