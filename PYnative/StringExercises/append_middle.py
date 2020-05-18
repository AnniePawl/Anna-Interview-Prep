# Given 2 strings, create new string by appending s2 into middle of s1

def append_middle(s1, s2):
  middle_index = (len(s1)//2)
  return s1[:middle_index] + s2 + s1[middle_index:]


print(append_middle("Anna", "Joey")) # AnJoeyna
print(append_middle("doom", "mood")) # domoodom
print(append_middle("nutellas", "bell")) # nutebellllas