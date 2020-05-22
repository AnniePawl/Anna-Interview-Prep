# Given string of digits, replace anything below 5 with 0, anythin above with a 1 


def fake_binary(x):
  nums = list(x)
  fake_binary = ""
  for num in nums:
    if num <= "5":
      fake_binary += "0"
    else: 
      fake_binary += "1"
  return fake_binary

def fake_binary2(x):
  return "".join('0' if num < '5' else '1' for num in x)

print(fake_binary("123456789")) # 000001111
print(fake_binary("9384")) # 1010
print(fake_binary2("9384")) # 1010