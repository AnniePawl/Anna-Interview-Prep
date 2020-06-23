# Given sequence of ints, each written on seperate line, determine len of sequence, which eds with 0  

a = int(input())
length = 0
while a != 0:
  a = int(input())
  length += 1
print(length)