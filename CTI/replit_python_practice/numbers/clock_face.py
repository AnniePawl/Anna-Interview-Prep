# Hour hand of analog clock turned a degrees since midnight. Determine angle by which minute hand turned since start of current hours. 

def clock_face(a):
  # 30 degrees per hour
  hour =  a / 30 
  remainder = a % 30  # in degrees
  return remainder * 12


print(clock_face(190)) # 120