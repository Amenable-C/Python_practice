# -*- coding: utf-8 -*-
"""BlackJack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17rG_Avy-Mae_E7blOibCafGQUP2MlxxS
"""

#Simple Blackjack Game
import random
total = 10000
for i in range(0, 5):
  cards = ["Di_A", "Di_1", "Di_2", "Di_3", "Di_4", "Di_5", "Di_6", "Di_7", "Di_8", "Di_9", "Di_10", "Di_J", "Di_Q", "Di_K", "He_A", "He_1", "He_2", "He_3", "He_4", "He_5", "He_6", "He_7", "He_8", "He_9", "He_10", "He_J", "He_Q", "He_K", "Sp_A", "Sp_1", "Sp_2", "Sp_3", "Sp_4", "Sp_5", "Sp_6", "Sp_7", "Sp_8", "Sp_9", "Sp_10", "Sp_J", "Sp_Q", "Sp_K", "Cl_A", "Cl_1", "Cl_2", "Cl_3", "Cl_4", "Cl_5", "Cl_6", "Cl_7", "Cl_8", "Cl_9", "Cl_10", "Cl_J", "Cl_Q", "Cl_K"]

  random.shuffle(cards)
  computer = []
  user = []
  for i in range(0, 3):
    computer.append(cards[i])
  for i in range(3, 6):
    user.append(cards[i])
  
  comP = 0
  useP = 0
  print("Your cards: %s, %s, %s" %(user[0], user[1], user[2]))

  for i in range(0, 3):
        if len(computer[i]) == 5:
            comP = comP + 10
        elif computer[i][3] == "A":
            comP = comP + 1
        elif computer[i][3] == "J" or computer[i][3] == "K" or computer[i][3] == "Q":
            comP = comP + 10
        else:
            comP = comP + int(computer[i][3])
  for i in range(0, 3):
        if computer[i][3] == "A":
            if comP + 10 < 22:
                comP = comP + 10

  for i in range(0, 3):
      if len(user[i]) == 5:
          useP = useP + 10
      elif user[i][3] == "A":
          useP = useP + 1
      elif user[i][3] == "J" or user[i][3] == "K" or user[i][3] == "Q":
          useP = useP + 10
      else:
          useP = useP + int(user[i][3])

  for i in range(0, 3):
      if user[i][3] == "A":
          if useP + 10 < 22:
              useP = useP + 10

  betOrDrop = input("Bet or Drop? (b/d)")
  if betOrDrop == "b":
      money = int(input("How much (Your total: %d)?" %total))
      if comP < 22 and comP > useP:
          total = total - money
          print("You lose... Your total: %d" %total)
      elif useP < 22 and comP < useP:
          total = total + (money * 2)
          print("Congrats! Your total: %d" %total)
      elif comP > 21 and useP < 22:
          total = total + (money * 2)
          print("Congrats! Your total: %d" %total)
      else:
          print("It is a tie! Your total: %d" %total)
  print()

print("Your total: %d" %total)