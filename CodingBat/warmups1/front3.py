# Given a string, front = first 3 characters. If string length is less than 3, front is whatever is there. Return new string which is 3 coppies of front.


def front3(str):
    front = str[:3]
    return front+front+front


print(front3('Java'))  # JavJavJav
print(front3('Chocolate'))  # ChoChoCho
print(front3('abc'))  # abcabcabc
