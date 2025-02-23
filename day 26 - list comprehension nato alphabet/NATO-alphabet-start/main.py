student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {}
for (index, row) in nato_csv.iterrows():
    index = row.letter
    row = row.code
    nato.update({index:row for therow in nato_csv})
print(nato)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
userinput = input("What word?")
nato2 = []
for c in userinput:
    c = c.capitalize()
    nato3 = {c:value for (key, value) in nato.items() if c == key}
    print(nato3)
    nato2.append(nato3)
print(nato2)
#     inputletters.append(c)
#     print(c)
#     print(inputletters)
# for _ in inputletters:
#     nato2 = {c:value for (key, value) in nato.items() if c == key} #[letter:code for (letter, code) in nato.items() if c == letter] #assigns random scores to students.
# print(nato2)
