# Given a string phrase/ sentence, return len of last word  

def len_last_word(str):
    str_list = str.split()
    if not str_list:
      return 0
    else:
      return len(str_list[-1])


print(len_last_word("Hello World")) # 5
print(len_last_word("")) # 0
print(len_last_word(" ")) # 0

# In one line 
return len(s.split()[-1] if s.split() else 0)