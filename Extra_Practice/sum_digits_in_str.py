# Sum digits in str. If digits consecutive, count as one number 


def sum_digits(str):
  temp = '0' 
  sum = 0 
  for char in str:
    if char.isdigit():
      temp += char
    else:
      sum += int(temp)
      temp = '0'
  # remember to add whatever is in temp to account for last char being digit
  return sum + int(temp)

print(sum_digits('ab11n2n3')) # 16 




