x = 10
y = 4
z = 159
print("Binary %d:" % x,bin(x))
print("Binary %d:  " % y,bin(y))
print("Binary %d:  " % z,bin(z))

print("Bitwise %d AND %d: " % (x,y), bin(x & y))
## 10 = 1010 Bitwise AND (& operator)
##  4 = 0100 =
## ---------
##         0


print("Bitwise %d OR %d: " % (x,y), bin(x | y), " ", x|y)
## 10 = 1010 Bitwise OR (| operator)
##  4 =  100 =
## ---------
##      1110

print("Bitwise %d XOR %d: " % (x,y), bin(x ^ y))
## 10 = 1010 Bitwise XOR (^ operator)
##  4 =  100 =
## ---------
##      1110

print("Bitwise NOT %d: " % (x), bin(~x), " base 10: %d" % ~x)
## 10 = 1010 Bitwise NOT (~ operator)
## ---------
##   -0b1011

print("Bitwise %d right shift: " % x, bin(x>> 2), " base 10: %d" % (x>> 2))
## 10 = 1010 Bitwise RIGHT SHIFT (>> operator)
##      >> 2
## ---------
##        10

print("Bitwise %d left shift: " % x, bin(x<< 4), " base 10: %d" % (x<< 4))
## 10 = 1010 Bitwise LEFT SHIFT (<< operator)
##      << 2
## ---------
##    101000