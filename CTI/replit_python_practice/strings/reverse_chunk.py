# Given string w/ 2 'h's, reverse sequence of chars inbetween. 

def reverse_chunk(s):
  first_h = s.find('h')
  last_h = s.rfind('h')

  return s[:first_h +1] + s[first_h + 1: last_h][::-1]  + s[last_h:]


# CTI Solution 
s = input()
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle[::-1] + right)

print(reverse_chunk('chedder chips')) #  ch c redde hips
print(reverse_chunk('In the hole in the ground there lived a hobbit')) #  ch c redde hips