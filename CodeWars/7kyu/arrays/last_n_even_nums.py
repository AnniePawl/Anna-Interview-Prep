# Given an array and n, return last n even numbers 

def evens(arr,n):
  evens = [x for x in arr if x % 2 == 0]
  return evens[-n:]

# One-liner
def evens2(arr,n):
  return evens = [x for x in arr if x % 2 == 0][-n:]


print(evens([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # [4, 6, 8]
print(evens([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2)) #  [-8, 26]