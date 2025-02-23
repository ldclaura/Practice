#hangman

#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
chosen_word = [x for x in chosen_word]
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.




#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-4 Make game repeat using while loop!!

#TODO-5 Make game say when you've won or not. keep track of wrong guesses.
#guess 1
guess = input("Guess a letter: ").lower()
#guess 1
guesses = ""
guesses2 = ""
guesses3 = ""
guesses4 = ""
guesses5 = ""
guesses6 = ""
guesses7 = ""
guesses8 = ""
guesses9 = ""
guesses10 = ""
guesses11 = ""
strikes = ""
for letter in chosen_word:
    if letter == guess:
        guesses += guess
    else:
        guesses += "_"
if guess.isalpha() == False:
    strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')

print(guesses)

#guess 2

while "_" in guesses:
    guess2 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess2:
            guesses2 += guess2
        elif letter == guess:
            guesses2 += guess
        else:
            guesses2 += "_"
    if guesses2 == guesses:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    
    print(guesses2)
    break

#guess 3

while "_" in guesses2:
    guess3 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses3 += guess3
        elif letter == guess2:
            guesses3 += guess2
        elif letter == guess:
            guesses3 += guess
        else:
            guesses3 += "_"
    if guesses3 == guesses2:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses3)
    break

while "_" in guesses3:
    guess4 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses4 += guess3
        elif letter == guess2:
            guesses4 += guess2
        elif letter == guess:
            guesses4 += guess
        elif letter == guess4:
            guesses4 += guess4
        else:
            guesses4 += "_"
    if guesses4 == guesses3:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses4)
    break

while "_" in guesses4:
    guess5 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses5 += guess3
        elif letter == guess2:
            guesses5 += guess2
        elif letter == guess:
            guesses5 += guess
        elif letter == guess4:
            guesses5 += guess4
        elif letter == guess5:
            guesses5 += guess5
        else:
            guesses5 += "_"
    if guesses5 == guesses4:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses5)
    break

while "_" in guesses5:
    guess6 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses6 += guess3
        elif letter == guess2:
            guesses6 += guess2
        elif letter == guess:
            guesses6 += guess
        elif letter == guess4:
            guesses6 += guess4
        elif letter == guess5:
            guesses6 += guess5
        elif letter == guess6:
            guesses6 += guess6
        else:
            guesses6 += "_"
    if guesses6 == guesses5:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses6)
    break
while "_" in guesses6:
    guess7 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses7 += guess3
        elif letter == guess2:
            guesses7 += guess2
        elif letter == guess:
            guesses7 += guess
        elif letter == guess4:
            guesses7 += guess4
        elif letter == guess5:
            guesses7 += guess5
        elif letter == guess6:
            guesses7 += guess6
        elif letter == guess7:
            guesses7 += guess7
        else:
            guesses7 += "_"
    if guesses7 == guesses6:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses7)
    break

while "_" in guesses7:
    guess8 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses8 += guess3
        elif letter == guess2:
            guesses8 += guess2
        elif letter == guess:
            guesses8 += guess
        elif letter == guess4:
            guesses8 += guess4
        elif letter == guess5:
            guesses8 += guess5
        elif letter == guess6:
            guesses8 += guess6
        elif letter == guess7:
            guesses8 += guess7
        elif letter == guess8:
            guesses8 += guess8
        else:
            guesses8 += "_"
    if guesses8 == guesses7:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses8)
    break
while "_" in guesses8:
    guess9 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses9 += guess3
        elif letter == guess2:
            guesses9 += guess2
        elif letter == guess:
            guesses9 += guess
        elif letter == guess4:
            guesses9 += guess4
        elif letter == guess5:
            guesses9 += guess5
        elif letter == guess6:
            guesses9 += guess6
        elif letter == guess7:
            guesses9 += guess7
        elif letter == guess8:
            guesses9 += guess8
        elif letter == guess9:
            guesses9 += guess9
        else:
            guesses9 += "_"
    if guesses9 == guesses8:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses9)
    break
while "_" in guesses9:
    guess10 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses10 += guess3
        elif letter == guess2:
            guesses10 += guess2
        elif letter == guess:
            guesses10 += guess
        elif letter == guess4:
            guesses10 += guess4
        elif letter == guess5:
            guesses10 += guess5
        elif letter == guess6:
            guesses10 += guess6
        elif letter == guess7:
            guesses10 += guess7
        elif letter == guess8:
            guesses10 += guess8
        elif letter == guess9:
            guesses10 += guess9
        elif letter == guess10:
            guesses10 += guess10
        else:
            guesses10 += "_"
    if guesses10 == guesses9:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses10)
    break
while "_" in guesses10:
    guess11 = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess3:
            guesses11 += guess3
        elif letter == guess2:
            guesses11 += guess2
        elif letter == guess:
            guesses11 += guess
        elif letter == guess4:
            guesses11 += guess4
        elif letter == guess5:
            guesses11 += guess5
        elif letter == guess6:
            guesses11 += guess6
        elif letter == guess7:
            guesses11 += guess7
        elif letter == guess8:
            guesses11 += guess8
        elif letter == guess9:
            guesses11 += guess9
        elif letter == guess10:
            guesses11 += guess10
        elif letter == guess11:
            guesses11 += guess11
        else:
            guesses11 += "_"
    if guesses11 == guesses10:
        strikes += "I"
    if strikes == "I":
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif strikes == "II":
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif strikes == "III":
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    elif strikes == "IIII":
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif strikes == "IIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    elif strikes == "IIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    elif strikes == "IIIIIII":
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\nYOU LOSE''')
    print(guesses11)
    break

if guesses.isalpha() == True:
    print("YOU WIN!")
if guesses2.isalpha() == True:
    print("YOU WIN!")
if guesses3.isalpha() == True:
    print("YOU WIN!")
if guesses4.isalpha() == True:
    print("YOU WIN!")
if guesses5.isalpha() == True:
    print("YOU WIN!")
if guesses6.isalpha() == True:
    print("YOU WIN!")
if guesses7.isalpha() == True:
    print("YOU WIN!")
if guesses8.isalpha() == True:
    print("YOU WIN!")
if guesses9.isalpha() == True:
    print("YOU WIN!")
if guesses10.isalpha() == True:
    print("YOU WIN!")
if guesses11.isalpha() == True:
    print("YOU WIN!")
    
