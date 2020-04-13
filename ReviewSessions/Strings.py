# Problem: Check if a string has all unique characters
# 'apple' --> False
# "cat" --> True

# Brute Force Option
# Time: O(n^2) b/c two for loops
# Space: 0(1)


def isUniqueBruteForce(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True


print(isUniqueBruteForce("apple"))
print(isUniqueBruteForce("cat"))


# Set Option
# Time: O(n) b/c one for loop
# Space: 0(n) b/c creating set

def isUnique(s):
    seen = set()  # Create an empty set
    for letter in s:  # Loop thru string
        if letter in seen:  # Check if letter is in set
            return False  # If already in set, return False
        else:
            seen.add(letter)    # If not, add to set
    return True


print(isUnique("dog"))
print(isUnique("button"))
