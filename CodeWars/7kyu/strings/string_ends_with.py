#  Return True is first argument ends with second argument 

# Brute Force
def ends_with(string, ending):
  ending_length = len(ending)
  if string[-ending_length:] == ending:
    return True
  else:
    return False

def ends_with_v2(string, ending):
  return string.endswith(ending)
  

print(ends_with('abcde', 'de')) # True
print(ends_with('abcde', 'ee')) # False
print(ends_with('Card', 'ard')) # True
print("V2")
print(ends_with_v2('abcde', 'de')) # True
print(ends_with_v2('abcde', 'ee')) # False
print(ends_with_v2('Card', 'ard')) # True