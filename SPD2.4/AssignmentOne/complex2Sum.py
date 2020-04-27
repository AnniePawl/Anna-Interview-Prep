# Given two arrays (a and b) of numbers and a target value(t), find a number from each array whose sum is closest to target(t).

# Example
# a = [9, 13, 1, 8, 2, 4, 0, 5], b = [3, 17, 4, 14, 6], t = 20
# solution = [13, 6] or [4, 17] or [5, 14]

a = [5,10]
b = [2,8]
t = 7


# For loop
  # Sum up each item from array a to each item in array b (one at a time)
  # Keep track of items in a variable - replace items in that variable if I come across sum that's closer to target
# Return one pair of items closest to target