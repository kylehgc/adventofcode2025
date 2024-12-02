lines = []
with open('input.txt') as file:
  lines = file.readlines()

reports = [[int(number) for number in line.split()] for line in lines]

def get_is_ascending(number_list):
  for index, number in enumerate(number_list):
    if(index == 0):
      continue
    previous_number = number_list[index -1]
    if(previous_number is not number):
      return number > previous_number    


def is_valid_report_step_one(number_list: list[int]):
  is_ascending = get_is_ascending(number_list)  
  for index, number in enumerate(number_list):
    if(index == 0):
      continue
    previous_number = number_list[index -1]
    if(previous_number is number):
      return False  
    if(is_ascending and previous_number > number):
      return False
    if(not is_ascending and previous_number < number):
      return False
    difference = abs(number - previous_number)
    if difference > 3:
      return False
  return True

def get_new_lists_is_valid(number_list: list[int], index: int):
  new_list_one = number_list[:index] + number_list[index + 1:]
  new_list_two = number_list[:index -1] + number_list[index:]
  new_list_three = number_list[:index + 1] + number_list[index + 2:]
  new_list_four = number_list[:index + 2] + number_list[index + 3:]
  new_list_five = number_list[:index - 2] + number_list[index -1:]

  return is_valid_report_step_one(new_list_one) or is_valid_report_step_one(new_list_two) or is_valid_report_step_one(new_list_three) or is_valid_report_step_one(new_list_four) or (is_valid_report_step_one(new_list_five))

def is_valid_report_step_two(number_list: list[int]):
  is_ascending = get_is_ascending(number_list)  
  for index, number in enumerate(number_list):
    if(index == 0):
      continue
    is_last_number = index == len(number_list) - 1
    previous_number = number_list[index -1]
    if(is_last_number):
      return True
    if(previous_number == number):
      new_list = number_list[:index] + number_list[index + 1:]
      return is_valid_report_step_one(new_list)
    if(is_ascending and previous_number > number):    
      return get_new_lists_is_valid(number_list, index)      
    if(not is_ascending and previous_number < number):
      return get_new_lists_is_valid(number_list, index)
    difference = abs(previous_number - number)
    if(difference > 3):
      return get_new_lists_is_valid(number_list,index)
  return True



are_safe_step_one = 0
for report in reports:
  is_safe =  is_valid_report_step_one(report)
  if(is_safe):
    are_safe_step_one = are_safe_step_one + 1
are_safe_step_two = 0
for report in reports:
  is_safe = is_valid_report_step_two(report)
  if(is_safe):
    are_safe_step_two = are_safe_step_two + 1

print(are_safe_step_one)
print(are_safe_step_two)
