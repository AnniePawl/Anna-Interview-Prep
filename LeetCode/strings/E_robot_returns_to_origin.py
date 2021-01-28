# Robot starting at position (0, 0) on a 2D plane. Given a sequence of moves, return True if ends up back at (0, 0) 

# Move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Pseudocode 
  # iterate over move sequence 
  # if U or D, increase of decrease origin[1]
  # if L or R, increase of decrease origig[0]
  # check if final == [0,0] 


# 0(N) --> 
def robot_returns(s):
  location = [0,0] # set origin
  for letter in s:
    if letter == 'D':
      location[1] -=1
    elif letter  == 'U':
      location[1] += 1
    elif letter == 'L':
      location[0] -=1
    elif letter =='R':
      location[0] +=1
    
  return location == [0,0]
  

print(robot_returns('UD')) # True (0,0)--> (1,1) -->(0,0)
print(robot_returns('UDDDU')) # False


class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0


# Clever 
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('R') == moves.count('L'))  & (moves.count('U') == moves.count('D'))