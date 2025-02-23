#rock paper scissors
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
import random
computerchoice = random.randint(0, 2)
yourchoice = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if int(yourchoice) == 0 and computerchoice == 0:
    print(f"{rock}\nComputer chose:\n{rock}\nIt's a draw.")
elif int(yourchoice) == 0 and computerchoice == 1:
    print(f"{rock}\nComputer chose:\n{paper}\nYou lose.")
elif int(yourchoice) == 0 and computerchoice == 2:
    print(f"{rock}\nComputer chose:\n{scissors}\nYou win.")

elif int(yourchoice) == 1 and computerchoice == 0:
    print(f"{paper}\nComputer chose:\n{rock}\nYou win.")
elif int(yourchoice) == 1 and computerchoice == 1:
    print(f"{paper}\nComputer chose:\n{paper}\nIt's a draw.")
elif int(yourchoice) == 1 and computerchoice == 2:
    print(f"{paper}\nComputer chose:\n{scissors}\nYou lose.")

elif int(yourchoice) == 2 and computerchoice == 0:
    print(f"{scissors}\nComputer chose:\n{rock}\nYou lose.")
elif int(yourchoice) == 2 and computerchoice == 1:
    print(f"{scissors}\nComputer chose:\n{paper}\nYou win.")
elif int(yourchoice) == 2 and computerchoice == 2:
    print(f"{scissors}\nComputer chose:\n{scissors}\nIt's a draw.")
