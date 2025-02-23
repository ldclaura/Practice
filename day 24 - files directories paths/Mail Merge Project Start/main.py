#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
char = "[name],"
count = 0
with open(r".\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    contents = file.read()


with open(r".\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    for line in file:
        print(line)
        # thename = file.readline()
        thename = line.replace('\n', '')
        thename2 = thename + ','
        replacement = contents.replace(char, thename2)
        print(replacement)
        with open(rf".\Mail Merge Project Start\Input\Letters\{thename}.txt", "w") as file:
            file.write(replacement)

# print(contents)
print("I accidentally deleted a folder or something and can't be assed fixing it so the program doesn't work")

# with open(rf".\Mail Merge Project Start\Input\Letters\{thename}.txt", "w") as file:
#     file.write(replacement)