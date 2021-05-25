#Grading System
nums = [0,]
score = 0

while True:
    score = int(input("Enter a score (-1 to quit): "))
    if score == -1:
        break
    nums[0:0] = [score]

count = len(nums) - 1
total = 0
highest = nums[0]
lowest = nums[0]

i = 0
while i < count:
  total = total + nums[i]
  if highest < nums[i]:
    highest = nums[i]
  if lowest > nums[i]:
    lowest = nums[i]
  i = i + 1

average = total / count

while True:
  num1 = input("1. The highest score\n2. The lowest score\n3. The average\n4. Quit\n>> Select the number: ")
  if num1 == '4':
    print("Bye~\n")
    break
  elif num1 == '1':
    print("The highest score is %s.\n" %highest)
  elif num1 == '2':
    print("The lowest score is %s.\n" %lowest)
  elif num1 == '3':
    print("The average is %s.\n" %average)
