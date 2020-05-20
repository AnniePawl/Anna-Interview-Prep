# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.


# Return number of valleys Gary walked thru 
# n:number of steps Gary takes 
# s:string describing his path 

def countingValleys(n,steps):
  # whenever upward AND number is 0, just finished a valley 
  num_of_valleys = 0
  altitude = 0 




print(countingValleys(8,"UDDDUDUU")) #1
print(countingValleys(8,"UDDDUDUUDDD")) #-3