# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.



def rotated_digits(n):
      count = 0
      rotated_dict = {0:0,1:1,2:5,3:None, 4:None, 5:2,6:9,7:None,8:8,9:6}
      ranges = [x for x in range(1,n+1)]
      rotated = [] # holds rotated nums < 10 
      rotated_digits = [] # holds rotated nums > 10

      
              

        
  
      # for i in range(len(ranges)):
      #     if ranges[i] != rotated[i] and rotated[i] != None:
      #         count +=1 
                
      # return count
        

print(rotated_digits(15)) 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 0 1 5 N N 2 9 N 8 6 01 11 51 N1 N1 21

#  10 11 12 13 14 15 
#  01 11 51 N1 N1 21
 
def joinit(list,l):
  new_nums = []
  for i in range(0,len(list),l):
    new_nums.append(''.join(str(x) for x in list[i:i+l]))
  return new_nums

# print(joinit([1,2,3,4,5,6],2)) # 12,34,56 
# print(joinit([1,2,3,4,5,6],3)) # 123, 456