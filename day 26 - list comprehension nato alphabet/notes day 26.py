#list and dictionary comprehensions
#nato phonetic alphabet

#list comprehension
#create list from list
#for loops
#instead of multiple lines you do:
# print("new_list = [new_item for item in list]")

# numbers = [1,2,3]
# new_list = []
# for n in list:
#     add_1 = n + 1

# new_list.append(add_1)
# print(new_list)

# new_list = [n + 1 for n in numbers] #new_list = [new_item for item in list]
# print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

#python sequences
#list
#range
#string
#tuple

numbers = range(1, 5)

# doubled_numbers = [number*2 for number in numbers]
doubled_numbers = [number*2 for number in range(1, 5)]
print(numbers)
print(doubled_numbers)

#conditional list comprehension
print("new_list = [new_item for item in list if test]")

names = ["Laura", "Alex", "Beth", "Eleanor"]
short_names = [name for name in names if len(name) < 5] #if name is shorter than 4
print(short_names)
uppercase_long_names = [name.upper() for name in names if len(name) >= 5]
print(uppercase_long_names)

#US STATES GAME
print("""if answer_state == "Exit":
    missing_states = []
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break""")
#INSTEAD:
print("""if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break""")

#DICTIONARY COMPREHENSION
print("new_dict = {new_key:new_value for item in list}")
#CONDITIONAL DICTIONARY COMPREHENSION
print("new_dict = {new_key:new_value for (key, value) in dict.items() if test}")
