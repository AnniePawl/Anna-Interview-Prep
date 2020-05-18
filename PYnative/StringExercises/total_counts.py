# Given a string input, count total chars, digits, and special symbols 

def total_counts(str):
  digits = sum(1 for digit in str if digit.isdigit())
 
  chars = sum(1 for char in str if char.isalpha())
  
  symbols = sum(1 for char in str if not char.isalnum())

  return {"Digits":digits, "Chars":chars, "Symbol": symbols}

print(total_counts("P@#yn26at^&i5vev"))