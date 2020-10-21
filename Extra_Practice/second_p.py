# Given a string, print the index of second occurance of "p". If only 1 p, print -1, if no ps, print -2


def second_occurance(str):
  first_p = str.find("p")
  if "p" not in str:
    return -2
  if str.count("p") == 1:
    return -1 
  else:
    return str.find('p', first_p + 1)

print(second_occurance("appropriate")) # 2
print(second_occurance("spare")) # -1
print(second_occurance("grouch")) # -2 