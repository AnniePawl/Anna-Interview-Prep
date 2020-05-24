# Given single string of comma separated values, return another string containing all characters except first and last 


def remove_first_last(string):
  string_list = string.split(",")
  remove = string_list[1:-1]
  return " ".join(remove) if remove else None

def remove_first_last2(string):
    return " ".join(string.split(",")[1:-1]) or None


print(remove_first_last("")) # None
print(remove_first_last("2")) # None
print(remove_first_last("1,2")) # None
print(remove_first_last("1,2,3,4")) # "2,3"

print(remove_first_last2("")) # None
print(remove_first_last2("2")) # None
print(remove_first_last2("1,2")) # None
print(remove_first_last2("1,2,3,4")) # "2,3"