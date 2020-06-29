# If string is palindrome, return 1, else return 0 

def palindrome(text):
# Remove punctuation and make lowercase 
  text = text.lower()
  punctuations = """?.",/: '"""
  for char in text:
    if char in punctuations:
      text = text.replace(char, '')
  
  return 1 if text == text[::-1] else 0
  
  
print(palindrome("anbA")) # 0
print(palindrome("otto")) # 1
print(palindrome("race car")) # 1
print(palindrome("grub")) # 0
print(palindrome("A man, a plan, a canal, Panama.")) # 1