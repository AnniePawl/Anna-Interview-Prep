# Given array, return new array of len n containing last n even numbers from original array in same order 


def even_nums_in_array(nums, n):
  evens = [num for num in nums if num % 2 == 0]
  return evens[-n:]


print(even_nums_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # [4, 6, 8]