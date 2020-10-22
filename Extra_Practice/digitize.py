# Turn num to reversed array of digits

def reverse(num):
  return [int(n) for n in str(num)][::-1]
 

print(reverse(1234)) # [4,3,2,1]

def digitize(num):
  map(int, str(n)[::-1])