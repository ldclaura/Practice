# file = open("my_file.txt")
# contents = file.read()
# print(contents)


# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    #use with as' so that you don't need file.close()
with open("my_file.txt", mode="w") as file:
    file.write("New Text")
    #writes, but deletes old text
with open("my_file.txt", mode="a") as file:
    file.write("Hello!!!!")
    file.write(f"\nHello!")
    #writes, doesn't delete old text (append)

with open("new_file.txt", mode="w") as file:
    file.write("This is a new file")
    #if file doesn't already exist, it will create one.


with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    lines = file.readlines()
    print(lines)
    #readlines() puts each line as strings in a list

