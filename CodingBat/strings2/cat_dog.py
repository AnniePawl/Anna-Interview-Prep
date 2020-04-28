# Return True is string "cat" and "dog" appear same number of times in given string


def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str)):
        if str[i:i+3] == "cat":
            cat_count += 1
        elif str[i:i+3] == "dog":
            dog_count += 1
    return(cat_count == dog_count)

# using built-in method .count()
def cat_dog_v2(str):
    return str.count("cat") == str.count("dog")


print(cat_dog("dogcat"))  # True
print(cat_dog("dogdogcat"))  # False
print(cat_dog("catdogcatdog"))  # True

print(cat_dog_v2("dogdogcat")) # False 
print(cat_dog_v2("dogdogcatcat")) # True 
