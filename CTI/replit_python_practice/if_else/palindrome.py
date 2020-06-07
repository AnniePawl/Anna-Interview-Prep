# Return YES if 4 digit num same backwards and forwards 


def palindrome(num):
  num_list = [int(x) for x in str(num)]
  if num_list[:2] == num_list[-2:][::-1]:
    return "YES"
  else:
    return "NO"

print(palindrome(1221)) # YES
print(palindrome(1234)) # NO