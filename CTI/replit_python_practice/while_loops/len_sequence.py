# Given sequence of ints, each written on seperate line, determine len of sequence, which eds with 0  

nums = []
line = input()
while line:
    nums.append(line)
    line = input()

sequence = nums[:nums.index("0")]
print(len(sequence))

