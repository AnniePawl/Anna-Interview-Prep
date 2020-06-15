# Days numbered 0(sunday) thru 6(saturday). Given an int betwen 1 and 365, find day or the week if jan 1 was Thurs

def day_of_week(date):
  days_of_week = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  day = 4 # Thurs @ index 4 in days of week list 
  for i in range(date-1):
    day += 1
  return (days_of_week[day % 7])

print(day_of_week(1)) #4 Thursday 
print(day_of_week(3)) #6 Saturday 
print(day_of_week(7)) #3 Wednesday 