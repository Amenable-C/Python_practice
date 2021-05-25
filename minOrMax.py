# Min or Max in a list
def max(list_nums):
  maximum = list_nums[0]
  for n in list_nums:
    if int(n) > int(maximum):
      maximum = n
  print("The maximum value = %s" %maximum)
def min(list_nums):
  minimum = list_nums[0]
  for n in list_nums:
    if int(n) < int(minimum):
      minimum = n
  print("The minimum value = %s" %minimum)


nums = input("List data: ")
nums = nums[1:-1]
list_nums = nums.split(", ")

while True:
  value = input("Input max or min to find the maximum or minimum value: ")
  if value == "max":
    max(list_nums)
  elif value == "min":
    min(list_nums)
  elif value == "":
    max(list_nums)
  else:
    print("Sorry, invalid input...")