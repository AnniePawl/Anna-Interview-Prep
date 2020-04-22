#  Given a string, return new string made of 3 copies of last two chars or original


def extra_end(str):
    return(str[-2:] * 3)


def extra_end2(str):
    end = str[-2:]
    return end + end + end


print(extra_end("Party"))  # tytyty
print(extra_end("Joy"))  # oyoyoy
print(extra_end("BUTTER"))  # ERERER
