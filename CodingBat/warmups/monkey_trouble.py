# Two monkeys (a, b), and parameters a_smile and b_smile indicate if they are smiling. We are in trouble if both or neither smiling. Return True if we are in trouble

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False


def monkey_trouble(a_smile, b_smile):
    return (a_smile == b_smile)


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
