# Write a function to reverse a string without using string slices or inbuilt methods


def reverse_string(str):
    reversed_string = ""
    for i in str:
        reversed_string = i + reversed_string
    return reversed_string


def reverse_string2(mystring):
    reversed_string = ""
    index = len(mystring)-1
    while index >= 0:
        reversed_string += mystring[index]
    return reversed_string


print(reverse_string("buttonhole"))
print(reverse_string("glue"))

print(reverse_string2("china"))
print(reverse_string2("georgia"))
