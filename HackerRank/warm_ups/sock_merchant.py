# Pair socks by color. Given an array of ints, determine how many pairs of socks w/ matching colors there are. Return an integer representing number of matching pairs of socks available. 

# def sockMerchant(n,ar):
#   pairs = 0 
#   for i in range(n-1):
#     if ar[i] == ar[i+1]:
#       pairs +=1
#   return pairs

def sockMerchant(n,ar):
  pairs = 0
  sock_set = set(ar)
  print("sock set: " + str(sock_set))
  for sock in sock_set:
    pairs +=  ar.count(sock) //2
  print("pairs")
  return pairs
  


print(sockMerchant(5, [1,1,2,4,4])) # 2 pairs
print(sockMerchant(10, [1,1,3,4,5,6,6,7,7,8])) # 3 pairs
print(sockMerchant(10, [1,1,3,4,5,6,6,7,7,7])) # 3 pairs 