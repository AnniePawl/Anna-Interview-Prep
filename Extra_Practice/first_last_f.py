# Given a string, return index of first and last occurance of "f". If no "f", return -1. 

def occurance(str):
  if "f" not in str:
    return -1
  elif str.count("f") == 1:
    return str.index("f")
  else:
    return str.find("f"), str.rfind("f")

print(occurance("hello")) # -1
print(occurance("comfort")) # 3
print(occurance("office")) # 1 2