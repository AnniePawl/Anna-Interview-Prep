# Remove every second elemnts from array 

def remove_second(arr):
  return arr[::2]

print(remove_second([1,2,3])) # [1,3]
print(remove_second(["when", "can", "i", "go"])) # when i