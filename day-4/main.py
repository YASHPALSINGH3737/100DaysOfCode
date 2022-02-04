import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("You chose incorrect option. Please choose from the given option")

choice2 = random.randint(0, 2)

if choice2 == 0:
  print(rock)
elif choice2 == 1:
  print(paper)
else:
  print(scissors)

if choice == choice2:
  print("It's a draw!")
elif choice == 0:
  if choice2 == 1:
    print("You lost!")
  else:
    print("You wins!")
elif choice == 1:
  if choice2 == 0:
    print("You wins!")
  else:
    print("You lost!")
elif choice == 2:
  if choice2 == 0:
    print("You lost!")
  else:
    print("You wins!")

