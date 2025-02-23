#higherorlower
import art
import data
import random
import os

def pick_the_number():
   """ Randomly selects number 1-50 """
   first = random.randint(0, 50)
   return first

def the_pick(pick_one_or_pick_two):
    """ Random pick from list based on number from pick_the_number


    pick_one = the_pick(first_pick_number)

    so basically its just the_pick(32) or some random number
    

    pick_two = the_pick(second_pick_number) """
    first_pick = data.data[pick_one_or_pick_two]
    return first_pick

def separate_data(da_pick, da_key):
    """ separate the data from the pick list.

    enter randomly picked person with desc, country, follower, out of 2, (da_pick)

    then enter the key - name, follower_count, country, description - as string (da_key)
    
    """
    for key, value in da_pick.items():
        if key == da_key:
            the_value = value
    return the_value

def game(game_name_1, game_follow_1, game_description_1, game_country_1, game_name_2, game_follow_2, game_description_2, game_country_2):
    print(art.logo)
    print(f"compare A: {game_name_1}, {game_description_1}, from {game_country_1}\nagainst B: {game_name_2}, {game_description_2}, from {game_country_2}")
    your_input = input("Who has more followers? Type 'A' or 'B':\n").lower()
    if your_input == "a":
        if game_follow_1 > game_follow_2:
            print(f"You win, {game_name_1} has {game_follow_1} followers, while {game_name_2} has only {game_follow_2} followers")
        else:
            print(f"You lose, {game_name_2} has {game_follow_2} followers, while {game_name_1} has only {game_follow_1} followers")
    if your_input == "b":
        if game_follow_2 > game_follow_1:
            print(f"You win, {game_name_2} has {game_follow_2} followers, while {game_name_1} has only {game_follow_1} followers")
        else:
            print(f"You lose, {game_name_1} has {game_follow_1} followers, while {game_name_2} has only {game_follow_2} followers")
    play_again = input("Would you like to play again? 'Y' or 'N':\n").lower()
    if play_again == "y":
        first_pick_number = pick_the_number()
        second_pick_number = pick_the_number()
        pick_one = the_pick(first_pick_number)
        pick_two = the_pick(second_pick_number)
        name1, follower_count_1, description1, country1, name2, follower_count_2, description2, country2 = separated_data(pick_one, pick_two)
        os.system('cls' if os.name == 'nt' else 'clear') #clear screen
        
        game(name1, follower_count_1, description1, country1, name2, follower_count_2, description2, country2)
        #NEED TO MAKE IT SO IT REDRAWS PEEPS
    else:
        pass

def separated_data(o, t):
    """ I probably overcomplicated this lol
     I made this so the game repeats """
    
    name1 = separate_data(o, "name")
    follower_count_1 = separate_data(o, "follower_count")
    description1 = separate_data(o, "description")
    country1 = separate_data(o, "country")

    name2 = separate_data(t, "name")
    follower_count_2 = separate_data(t, "follower_count")
    description2 = separate_data(t, "description")
    country2 = separate_data(t, "country")
    return name1, follower_count_1, description1, country1, name2, follower_count_2, description2, country2


first_pick_number = pick_the_number() #just selects number

second_pick_number = pick_the_number() #different number

#selects the two to compare
pick_one = the_pick(first_pick_number)
pick_two = the_pick(second_pick_number)



name1, follower_count_1, description1, country1, name2, follower_count_2, description2, country2 = separated_data(pick_one, pick_two)


separated_data(pick_one, pick_two)
game(name1, follower_count_1, description1, country1, name2, follower_count_2, description2, country2)
#compare A: Cristiano Ronaldo, a Footballer, from Portugal
#against B: Vin Diesel, a Actor, from United States.
#who has more followers? Type 'A' or 'B':



# first_pick = data.data[first_pick_number] #first dictionary
# second_pick = data.data[second_pick_number]
# print(first_pick)
# print(second_pick) #second dictionary


#USE DEBUG

        


#compare A: Cristiano Ronaldo, a Footballer, from Portugal
#against B: Vin Diesel, a Actor, from United States.
#who has more followers? Type 'A' or 'B':


#do this instead of globalising a variable
# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")