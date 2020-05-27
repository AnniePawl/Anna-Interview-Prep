#  Given 3 integers (a,r,n), return sum of first n elements in which each element is sum if given int a and a number of occurances of given int r based on position within sequence. 


def arithmetic_seq(a,r,n):
  count = 1
  sum = a
  while count < n:
    sum += a + r*count 
    count +=1
  return sum

def arithmetic_seq2(a,r,n):
  return n * (a + a + (n-1)* r) /2


print(arithmetic_seq(2,3,5)) # 40
# a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r) 
# 2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40

print(arithmetic_seq2(2,3,5)) # 40