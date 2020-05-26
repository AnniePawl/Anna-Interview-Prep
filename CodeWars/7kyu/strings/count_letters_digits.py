# Given string, return count of how many letters and digits there are 

def count_letters_digits(string):
  return sum(1 for char in string if char.isalnum()) 


def count_letters_digits2(string):
  return sum(map(str.isalnum,string))

print(count_letters_digits('n!!ice!!123')) # 7
print(count_letters_digits('')) # 0
print(count_letters_digits('!@#$%^&`~.')) # 0
print(count_letters_digits('!@#$%^&`~.')) # 0
print(count_letters_digits('de?=?=tttes!!t')) # 8