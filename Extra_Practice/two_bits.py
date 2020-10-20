# Given a 2 bit int, print left bit by using division operator, and right bit by using remainder operator

def two_bits(num):
  binary = []
  binary.append(num //2)
  binary.append(num % 2)
  return " ".join(map(str,binary))

print(two_bits(3)) # 1 1
print(two_bits(2)) # 1 0 


def two_bits2(num):
  return (num//2, num%2)

print(two_bits2(3)) # 1 1