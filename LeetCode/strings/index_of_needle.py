# Return index of first occurance of "needle in haystack"
# If needle not in hackstack, return -1


def needle_index(haystack, needle):
  return haystack.index(needle) if needle in haystack else -1

print(needle_index("hello", "ll")) # 2
print(needle_index("banana", "z")) # -1
print(needle_index("banana", "a")) # 1


# Brute Force 
def needle_index_brute(haystack, needle):
  if len(needle) == 0:
    return 0 
  for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle) == needle]:
      return i 
  return -1 