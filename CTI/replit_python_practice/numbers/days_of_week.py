# Days numbered 0(sunday) thru 6(saturday). Given an int betwen 1 and 365, find day or the week if jan 1 was Thurs

def day_of_week(date):
  date = 1
  day = 4
  for date in range(0,366):
    day = date //7 -7
  return day
 
  

print(day_of_week(1)) #4
print(day_of_week(3)) #6