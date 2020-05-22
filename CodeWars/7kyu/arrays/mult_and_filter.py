# Take in sequence of numbers and multiplier. Filter all non-numeric values multiply the rest by given multiplier 

def mult_and_filter(sequence, multipler):
  # works for numbers only
  # return [val * multipler for val in sequence]
  string_list = list(map(str,sequence))
  nums_string = [value for value in string_list if value.isdigit()]
  nums_int = list(map(int, nums_string))
  multiplied = [value * multipler for value in nums_int]
  return multiplied

print(mult_and_filter([1,2,3,4],3)) # [3,6,9,12]
print(mult_and_filter([True, 5, "hi", {}, 10],5)) # [25,50]


# BEST SOLUTION
def mult_and_filter2(sequence, multipler):
  return [num * multipler for num in sequence if type(num) in (int,float)]


print(mult_and_filter([1,2,3,4],3)) # [3,6,9,12]
print(mult_and_filter([True, 5, "hi", {}, 10],5)) # [25,50]
