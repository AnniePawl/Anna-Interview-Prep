# What is smallest number that can be EVENLY divisible by all numbers from 1-20. 

# Examples 2520 is smallest num that can be evenly divided by numbers from 1-10

def smallest_divisible(range):
  n = 3   # start at n
  current_num = n + 1   # current num = n + 1
  while True:
    highly_divisible = True 
      # for each test num from 1 thru n:
    for test_num in range(1, n+1):
      # is current num divisible by test_num ?
      if current_num % test_num != 0:
        # if yes, move on to next num 
        current_num += 1
        highly_divisible = False
        break 
        # if no, increment current num by 1 
      if highly_divisible:
        print(current_num)
        break
        


print(smallest_divisible(20))