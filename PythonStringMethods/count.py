# .count()
# Returns number of times specified value appears


text = "I love apples so fucking much omg apples apples everywhere"
print(text.count("apples"))  # 3

cats_count = "catcatcatcatcat"
print(cats_count.count("cat")) # 5


# This method also works on LISTS
numbers = [1,2,2,3,3,3]
print(numbers.count(1)) # 1
print(numbers.count(2)) # 2
print(numbers.count(3)) # 3