# Given array of ones and zeros, convert binary value to an integer

def binary_to_decimal(num_array):
  # one = "on", zero = "off"
  # reverse array so index corresponds w/ power 
  reversed_num_array = num_array[::-1]
  count = 0 # initialize count 
  for i, value in enumerate(reversed_num_array):
    # print(i)
    if value == 1:
      count += 2**i
  return count
 

  

print(binary_to_decimal([0,0,0,1])) #1
print(binary_to_decimal([0,0,1,1])) #3
print(binary_to_decimal([1,1,1,1])) #15