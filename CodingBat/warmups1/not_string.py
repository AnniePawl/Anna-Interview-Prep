# Given a string, return new string where "not" has been added to the front. However, if string already begins w/ "not", return string unchanged


def not_string(str):
    if str[:3] == "not":
        return str
    else:
        return "not " + str


print(not_string('candy'))  # not candy
print(not_string('meat'))  # not meat
print(not_string('not bad'))  # not bad
