# 9. Given a str, return sum and average of digits that appear in str, ignore all chars

def sum_average(s1):
  temp = "0"
  sum = 0 
  for char in s1:
    if char.isdigit():
      temp += char
    else:
      sum += int(temp)
      temp = "0"
  return sum + int(temp)
 

print(sum_average("English = 78 Science = 83 Math = 68 History = 65")) # Sum = 294 Average = 73.5