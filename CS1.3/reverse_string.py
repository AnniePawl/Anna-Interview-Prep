# Write a function that will reverse a string using a stack


def reverse_string_stack(str):
    my_stack = []
    reversed_string = ""
    for letter in str:
        my_stack.append(letter)
    while len(my_stack) != 0:
        letter = my_stack.pop(-1)
        reversed_string += letter
    return reversed_string


print(reverse_string_stack("hello"))
print(reverse_string_stack("abc"))
