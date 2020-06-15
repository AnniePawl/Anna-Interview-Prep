# Server handles tasks first come first server. Each day, server runs tasks for T min. Given time each task takes, how many will you finish in a day. 


def server_time_check(task_config, task_times):
  time_limit = task_config[1]
  num_tasks = 0 
  for item in task_times:
    time_limit -= item
    if time_limit > 0:
      num_tasks +=1
  return num_tasks

  

## Please do not change the code below this line
## These lines are how the tests interact with the code

# task_config = input("Please input the number of tasks, and the maximum total execution time:")
# task_times = input("Please input the execution times of each task, seperated with a space:")

print(server_time_check([6,180], [45,30,55,20,80,20])) #4 
print(server_time_check([10,60], [20,7,10,8,10,27,2,3,10,5])) #5

numbers = input()
print([int(num) for num in str(numbers).split()])