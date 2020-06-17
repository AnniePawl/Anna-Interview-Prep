# Accept and display 3 strings from user 


# Will throw error if you don't enter eactly 3 
str1, str2, str3 = input("Enter 3 names: ").split()
print(str1, str2, str3)



# Will return list where each item is a name 
# .split will separate at space. Without it, each item in list will be an individual letter
pets = [name for name in str(input("Enter pets names")).split()]
print(pets)