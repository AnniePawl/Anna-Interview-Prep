# You're given sequence of ints, each written on seperate line. Sequence end with 0. Sum sequence 


a = int(input())
sum = 0 
while a != 0:
  sum += a
  a = int(input())
print(sum)