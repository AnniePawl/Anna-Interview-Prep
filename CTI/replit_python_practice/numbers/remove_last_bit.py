# Given 2 input numbers, print two numbers with binary value shifted to teh right by 1 bit 


# Shorthand - Try using left shift / right shift bitwise operation 
def remove_last_bit(x,y):
  

print(remove_last_bit(3,5)) # 1,2
# 3 is 0b11 in binary, when right shifted by 1 bit will become 0b01, which is 1 and 5 is 0b101 in binary and when right shifted by 1 bit will become 0b10, which is 2. Hence the output 1 2
# print(remove_last_bit(6,8)) # 3,4
# print(remove_last_bit(5,8)) # 2,4