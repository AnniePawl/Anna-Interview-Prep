def reverse(str):
    '''reverse a string'''
    return str[::-1]


def num_to_string(num):
    '''turn num into string'''
    return str(num)


if __name__ == "__main__":
    print(reverse("hello"))
    print(type(num_to_string(15)))
