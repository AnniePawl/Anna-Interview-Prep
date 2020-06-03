# Print first digit to right of decimal 

def decimal(float):
    dec_list = str(float).split(".")
    return (dec_list[1])[0]

def decimal2(float):
  return(int(float(float)) * 10 % 10)


print(decimal(1.78)) # 7
print(decimal(2.45)) # 4
