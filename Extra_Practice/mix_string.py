# Cut string in half. If odd, leave middle w/ first chunk. Swap halves 


def swap_halves(str):
  if len(str)% 2 == 0:
    return str[len(str)//2:] + str[:len(str)//2]
  else:
    return str[len(str)//2 +1:] + str[:len(str)//2+1]

print(swap_halves("Anna")) # naAn
print(swap_halves("Qwerty")) # rtyQwe
print(swap_halves("Gross")) # ssGro