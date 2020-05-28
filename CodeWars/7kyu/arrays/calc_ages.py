# Given sum and difference of two peoples ages, return individual ages as pair (oldest, first)


def get_ages(sum_, difference):
  x = (sum_ + difference)/2 
  y = (sum_ - difference)/2 

  return (x,y)

print(get_ages(24,4)) # (14,10)
