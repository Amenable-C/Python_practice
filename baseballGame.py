# Baseball game
import random

fix = []
n = 0
while n < 3:
  fix.append(random.randint(0,9))
  n = n + 1
#print(fix)
trial = 0

while True:
  trial = trial + 1
  guess = input("Guess three numbers: ")
  guessS = guess.split(" ")
  #print(guessS)
  s = 0
  b = 0

  for i in range(0, 3):
    if fix[i] == int(guessS[i]):
      s = s + 1

  for i in range(0, 3):
    for k in range(0, 3):
      if fix[i] == int(guessS[k]) and i != k :
        b = b + 1

  print("%dS %dB" %(s, b))
  if s == 3:
    break

print("Congratulations!")
print("You won with %d trials" %trial)