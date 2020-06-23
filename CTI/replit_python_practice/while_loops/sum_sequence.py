# Given sequence of nums written on seperate lines, where sequence ends at 0, return sum of sequence 

a = int(input())
sum = 0 
while a != 0:
  sum += a 
  a = int(input())
print(sum)
