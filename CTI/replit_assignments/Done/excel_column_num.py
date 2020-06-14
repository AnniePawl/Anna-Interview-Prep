# Each letter occupies column in spreadsheet. Return Column of each letter 


# Try w/ base 26 
def excel_column_to_number(column):
  value = 0
  reversed_column_list = list(column)[::-1]
  for i in range(len(reversed_column_list)):
    # print(reversed_column_list[i])
    value += (ord(reversed_column_list[i])-64) * (26**i)
  return value


# print(excel_column_to_number("A")) # 1
# print(excel_column_to_number("Z")) # 26
# print(excel_column_to_number("AB")) # 28


def excel_column_to_number2(column):
  value = 0 
  reversed_column_list = list(column)[::-1]
  for i, j in enumerate(reversed_column_list):
    value += (ord(j) -64) * (26**i)
  return value

print(excel_column_to_number2("A")) # 1
print(excel_column_to_number2("Z")) # 26
print(excel_column_to_number2("AB")) # 28





# def Number(C):
#   return ord(C) - ord("A") + 1;

# Column = "AD"

# x = Number(Column[0]) * 26 
# y = Number(Column[1])
# n = x + y
# print(Number(Column))

# def two_letters(letters):
  # position = 0
  # letter_list = [letter for letter in letters]
  # # First letter
  # first_letter_position = ord(letter_list[0]) - 64
  # position += 26 * first_letter_position
  # position += ord(letter_list[1]) -64
  # return position