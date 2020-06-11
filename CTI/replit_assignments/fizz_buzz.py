# Given an input, print all nums up to and including input. If divisible by 3, print "fizz" instead. If divisible by 5, print "buzz". If divisible by both 4 and 5, print "fizzbuzz"

def fizzbuzz(num):
  for num in range(1,num+1):
    if num % 3 == 0 and num % 5 == 0:
      print("fizzbuzz")
    elif num % 3 == 0:
      print("fizz")
    elif num % 5 == 0:
      print("buzz")
    else:
      print(num)


# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)

print(fizzbuzz(5)) # 1,2,fizz,4,buzz
print(fizzbuzz(7)) # 1,2,fizz,4,buzz


