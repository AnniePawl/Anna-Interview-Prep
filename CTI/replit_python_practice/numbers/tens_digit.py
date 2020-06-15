# Given in int, print tens digit

def tens_place(num):
  reversed = [int(x) for x in str(num)][::-1]
  if len(reversed) >=2 :
    return reversed[1]
  return 0

print(tens_place(1234)) 


# CTI Solution 
print(int(input()) % 100 // 100)