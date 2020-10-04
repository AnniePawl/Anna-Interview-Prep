# Given a word, return index of first and last occurance of "f"
# Return -1 if no occurance of f 


def occurances(word):
  if "f" not in word:
    return -1
  if word.count("f") == 1:
    return word.index("f")
  else:
    return word.index("f"), word.rfind("f")

print(occurances("office")) # 1 2
print(occurances("comfort")) # 3
print(occurances("bug")) # 3