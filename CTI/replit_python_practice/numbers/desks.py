# Desks can fit 2 students. Program reads 3 ints (a,b,c) representing number of students in each of 3 classes. Return total number of desks that can be purcahsed to accommodate all 3 classes
import math 

def desks(a,b,c):
  total_desks = 0
  class_list = [a,b,c]
  for num in class_list:
    total_desks += math.ceil(num/2)
  return total_desks


print(desks(20,21,22)) # 32 

# CTI Solution 
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)
