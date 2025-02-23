
import random

attempts = 0
def random_number():
  return random.randint(1, 100)
number = random_number()

def hard():
  return attempts + 4
def easy():
  return attempts + 9
def game(the_attempt):
  print(f"You have {the_attempt + 1} attempts remaining to guess the number.")
  guess = input("Make a guess: \n")
  guess = int(guess)
  #incorporate attempts number (the_attempt)

  while guess != number:
      
    for attempt in range(the_attempt):
      if guess > number:
        print("Too high")
        guess = input("Make a guess: \n")
        guess = int(guess)
      elif guess < number:
        print("Too low")
        guess = input("Make a guess: \n")
        guess = int(guess)
    if guess == number:
      pass
    else:
      print(f"you've run out of guesses, you lose. \n the answer was {number}")
      break
  else:
    print(f"you got it! the answer was {number}")
    pass





def start():

#number guessing game
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
  if difficulty == "easy":
    attempts = easy()
    game(attempts)

  elif difficulty == "hard":
    attempts = hard()
    game(attempts)

  else:
    print("That was not an option.")

start()

playagain = input("Would you like to play again?")
if playagain == "yes":
  random_number()
  number = random_number()
  start()
else:
  pass
#too high
#too low
#guess again

#you got it! the answer was
#you've run out of guesses, you lose.


#do this instead of globalising a variable
# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

