#  2 size bricks ( 1" & 5"). We want to make a wall "goal" inches long. Return True if possible make goal w/ some combo of bricks. 

def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal

print(make_bricks(3,1,8)) # True 
print(make_bricks(3,1,9)) # False
print(make_bricks(3,2,10)) # True


# Initial Solution :
# Issue - does not account for big brick fixed size 
# return goal - (small + big * 5) <=0


# In this case, goal has to be multiple of 5
def big_brick(big_brick, goal):
  return (goal%5 == 0) and (goal-(big_brick * 5 )<= 0)

# print(big_brick(2,10)) # True (multiple of 5)
# print(big_brick(3,12)) # False
