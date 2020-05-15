def food_required(serving_size, child_count):
  daily_serving = serving_size * child_count
  # monthly_servings = daily_servings * 30 days. Expected output --> 600  
  monthly_serving = daily_serving * 30
  # return montly servings needed
  return monthly_serving

   
print(food_required(2,10))