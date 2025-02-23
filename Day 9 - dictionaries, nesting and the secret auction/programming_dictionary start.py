programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

#retrieving items from dictionary
print(programming_dictionary["Bug"])
#adding piece of data
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create empty dictionary
empty_dictionary = {}

#wipe existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#loop through dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])