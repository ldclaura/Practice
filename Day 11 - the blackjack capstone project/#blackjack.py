#blackjack

#card game
#add up cards to largest number without going over 21
#if they go up to more than 21 = bust (lose)
#2-10 count as face value
#jack queen king is 10
#ace can be 1 or 11 (u chose)

#you're playing against the dealer
#dealer has 2 cards but if its <17 then grabs another card
import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def game():
    """ Plays the game!!! """
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = []
    dealers_cards = []

    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))

    dealers_cards.append(random.choice(cards))
    dealers_cards.append(random.choice(cards))
    print(f"Your cards: {your_cards}")

    sum_of_your_cards = sum(your_cards)
    sum_of_dealers_cards = sum(dealers_cards)


    for eleven in range(len(your_cards)):
        if your_cards[eleven] == 11:
            if sum_of_your_cards > 21:
                your_cards[eleven] = 1
    for eleven in range(len(dealers_cards)):
        if dealers_cards[eleven] == 11:
            if sum_of_dealers_cards > 21:
                dealers_cards[eleven] = 1


    gameend = False


    #NOTE add option to change 11 to a 1
    while sum_of_your_cards < 21:
        choice = input("would you like to draw or sit? \n").lower()
        if choice == "draw":
            your_cards.append(random.choice(cards))
            sum_of_your_cards = sum(your_cards)
            for eleven in range(len(your_cards)):
                if your_cards[eleven] == 11:
                    if sum_of_your_cards > 21:
                        your_cards[eleven] = 1

            print(your_cards)
            sum_of_your_cards = sum(your_cards)
        elif choice == "sit":
            break #sit doesn't work?
    else:
        if sum_of_your_cards == 21:
            print("your win")
            gameend = True
        elif sum_of_your_cards > 21:
            print("you lose")
            gameend = True
        #dealer has 2 cards but if its <17 then grabs another card

    while sum_of_dealers_cards < 17 and gameend == False:
        print(f"Dealers cards: {dealers_cards}")
        dealers_cards.append(random.choice(cards))

        for eleven in range(len(dealers_cards)):
            if dealers_cards[eleven] == 11:
                if sum_of_dealers_cards > 21:
                    dealers_cards[eleven] = 1

        sum_of_dealers_cards = sum(dealers_cards)
    else:
        if sum_of_dealers_cards > 21 and gameend == False:
            print(f"Dealers cards: {dealers_cards}")
            print("you win")
        elif sum_of_dealers_cards == sum_of_your_cards and gameend == False:
            print(f"Dealers cards: {dealers_cards}")
            print("draw")
        elif sum_of_dealers_cards > sum_of_your_cards and gameend == False:
            print(f"Dealers cards: {dealers_cards}")
            print("you lose")
        elif sum_of_dealers_cards < sum_of_your_cards and gameend == False:
            print(f"Dealers cards: {dealers_cards}")
            print("You win")
        elif gameend == True:
            print(f"Dealers cards: {dealers_cards}")
        else:
            print(f"dealers cards are::::: {dealers_cards}")
    
    # print(f"this is dealers cards {dealers_cards}")
    playagain = input("Would you like to play again? yes or no \n").lower()
    if playagain == "yes":
        os.system('cls' if os.name == 'nt' else 'clear') #clear screen
        game()
    else:
        pass
game()
# for card in your_cards:
#     sum_of_your_cards = sum(your_cards)
#     print(sum_of_your_cards) #

#HINT 4
# def deal_card():
#     """ Returns a random card from the deck """
#     cards = []
#     card = random.choice(cards)
#     return card

# #HINT 5 deal the user and computer 2 cards each using deal_card()
# user_cards = []
# computer_cards = []

# for _ in range(2):
#     new_card = deal_card()
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#HINT 6 and 7 create a function called calculate_score() that takes a list of cards as input and returns the score. sum() func
# def calculate_score(cards):

#     if 11 in cards and 10 in cards and len(cards) == 2:
#         return 0 #blackjack, hand with only 2 carsd: ace + 10) 0 = blackjack
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0 #same thing

    # return sum(cards)

#HINT 8 inside calculate_score() check for an 11 (ace) if the score is already over 21 remove the 11 and replace it with a 1. you might need to look up append and remove

    # if 11 in cards and sum(cards) > 21:
    #     cards.remove(11)
    #     cards.append(1)

    #     return sum(cards)

#HINT 9
#calling the funcs
#move func near top
# user_score = calculate_score(user_cards)
# computer_score = calculate_score(computer_cards)

# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True




