# For i in range(0,120):
# print(i, format(i, '08b))

x = 25
base = 10 

print(x, ":", format(x,'08b'))

while True:
  print (x , '/', base)
  print ("   ",int(x/base),'-', x%base);
  #x = int(x/base);
  x = x >> 1;
  if x == 0:
    break;
