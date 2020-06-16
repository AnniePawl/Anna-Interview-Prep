# One first day, run x miles. On second day, run y miles. calc num of days needed to reach required distance if you increase distance by 10 % from previous day. 

def days_to_distance(starting_distance,total_distance):
  days = 1
  while starting_distance < total_distance:
    starting_distance += starting_distance * .1
    days += 1
  return days
  

print(days_to_distance(10,30)) # 13 