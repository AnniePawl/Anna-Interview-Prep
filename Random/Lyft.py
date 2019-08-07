# Versioned Key-Vlaue Pairs

# 60 minutes to code
# Use external resources like StackOverflow and Rosetta Code
# Graded on correctness (40%)
# Clean Code (35%)
# Performance (25%)

# Build simple key-value store for storing integers (keys are strings, values are integers) and a global version. You will store data in memory

# Version number is an integer that increases monotonically. Every time any key is written with a value, the version number is increased. First write is version number 1. Second write is version 2...

# The store supports three operations. First is PUT, which returns version number of this write. Second operation is the simple GET, which returns last value  mapped to key. Third operation is versioned Get, which takes a key and a versino number and returns value mapped to the key at the time of the version number.

# Input contains three types of commands corresponding to three operations supported by store.
# Assume all inputs are case senstative.

# Sample Input
PUT key1 5
PUT key2 6
GET key1
GET key1 1
GET key2 2
PUT key1 7
GET key1 1
GET key1 2
GET key1 3
GET key4
GET key1 4

# Sample Output
PUT(  # 1) key1 = 5
PUT(  # 2) key2 = 6
GET key1=5
GET key1(  # 1) = 5
GET key2(  # 2) = 6
PUT(  # 3) key1 = 7
GET key1(  # 1) = 5
GET key1(  # 2) = 5
GET key1(  # 3) = 7
GET key4= < NULL >
GET key1(  # 4) = 7
