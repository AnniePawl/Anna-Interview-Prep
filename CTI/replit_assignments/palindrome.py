# If string is palindrome, return 1, else return 0 

def palindrome(text):
  text = "".join(text)
  return text
  # left_index = 0
  # right_index = len(text)-1
  # # Ensure middle hasn't been surpased
  # while left_index <= right_index:
  #     if text[left_index] != text[right_index]:
  #         return 0
  #     else:
  #         left_index += 1
  #         right_index -= 1
  # return 1


  
  
print(palindrome("anba")) # 0
print(palindrome("otto")) # 1
print(palindrome("race car")) # 1
print(palindrome("grub")) # 0
print(palindrome("A man, a plan, a canal, Panama.")) # 1