# For each num in sequence, print YES if seen yet, NO if not seen 

def seen(nums):
  num_set = set()
  for num in nums: 
    if num in num_set:
      print ("YES")

    else:
      print("NO")
      num_set.add(num)
  



print(seen([1,2,3,2,3,4]))