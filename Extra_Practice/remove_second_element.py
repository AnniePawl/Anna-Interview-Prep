# Remove every second element of an array 

# Easiest Option 
def rem_second(arr):
  return arr[::2]


def remove_second(arr):
  new_arr= []
  for i, j in enumerate(arr):
    if i % 2 == 0:
     new_arr.append(j)
  return (new_arr)
    
print(remove_second(["hi", "bye","hello","goodbye"])) # "hi" "hello"
print(remove_second([1,2,3,4,5,6])) # 1,3,5