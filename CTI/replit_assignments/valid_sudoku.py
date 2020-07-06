# Validate sudoku- only filled cells need to be validated according to following rules 
# Each row and column must contain digits 1-9 w/o repetition 
#  Each 3x3 subbox much contain digits 1-9 w/o repetition 


def validate_sudoku(board):
  # Validate each row 
  for row in board:
    if not validate_row(row):
      return False
   # Validate each column 
    if not validate_columns(board):
      return False
  # Validate each sub-box 
    if not validate_box(board):
      return False
  return True

def  validate_row(row):
  seen_numbers = set()
  for number in row:
    if number != "." and number in seen_numbers: # 0(1) to check set
      return False 
    else:
      seen_numbers.add(number)
  return True


def validate_columns(board):
  for col_index in range(0,9):
    column =[]
    for row_index in range(0,9):
      column.append(board[row_index][col_index])
    if not validate_row(column):
      return False 
  return True

def validate_box(board):
  for row_index in range(0,7,3): # remember range not inclusive
    for col_index in range(0,7,3):
      box = [
        board[row_index + 0][col_index + 0], 
        board[row_index + 0][col_index + 1],
        board[row_index + 0][col_index + 2], 

        board[row_index + 1][col_index + 0], 
        board[row_index + 1][col_index + 1],
        board[row_index + 1][col_index + 2],

        board[row_index + 2][col_index + 0],
        board[row_index + 2][col_index + 1],
        board[row_index + 2][col_index + 2] 
      ]
      if not validate_row(box):
        return False 
  return True


sudoku1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
] # Valid (True)

sudoku2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# Not Valid (False)

print('validate row function')
print(validate_row(["5","3",".",".","7",".",".",".","."])) # True
print(validate_row(["5","3",".","5","7",".",".",".","."])) # False

print('validate column function')
print(validate_columns(sudoku1)) # True 
print(validate_columns(sudoku2))  # False

print(validate_box(sudoku1))


print('validate whole sudoku')
print(validate_sudoku(sudoku1)) # True
print(validate_sudoku(sudoku2)) # False
