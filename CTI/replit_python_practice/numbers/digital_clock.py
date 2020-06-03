# Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?

# The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.

# takes in how many minutes past midnight 
def clock(min):
  return str(min // 60) + " " + str(min % 60)



print(clock(150)) # 2 30
