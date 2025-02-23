#note: this program is shit and doesn't work properly. I got sick of making it so i gave up.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(plain_text, shift_amount, the_direction): #prob rename parameters so they aren't same as the arguments (stop confusion)
    text = plain_text
    shift = shift_amount
    direction = the_direction
    cipherText = ""
    codeordecode = ""

    for ch in text:
        if ch.isalpha():
            if direction == "encode":
                  #examines a string for alphabetical characters and returns True only if the string contains all alphabetical characters
                stayInAlphabet = ord(ch) + shift
                codeordecode = "cyphered text" #ord() returns the number representing the unicode code of a specified character. unicode of char + shift number
            elif direction == "decode":
                stayInAlphabet = ord(ch) - shift
                codeordecode = "decyphered text"
            if stayInAlphabet > ord('z'): #if its greater than z - numbers of alphabet. (so z turns back to a, b, c.)
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet) #obtain any character for which the unicode code value is known.
            cipherText += finalLetter
    print(f"Your {codeordecode} is: ", cipherText)
    return cipherText

# def decrypt(text, shift): #prob rename parameters so they aren't same as the arguments (stop confusion)
#     text = text
#     shift = shift
#     cipherText = ""
#     for ch in text:
#         if ch.isalpha():  #examines a string for alphabetical characters and returns True only if the string contains all alphabetical characters
#             stayInAlphabet = ord(ch) - shift #ord() returns the number representing the unicode code of a specified character. unicode of char + shift number
#             if stayInAlphabet > ord('z'): #if its greater than z + numbers of alphabet.
#                 stayInAlphabet -= 26
#             finalLetter = chr(stayInAlphabet) #obtain any character for which the unicode code value is known.
#             cipherText += finalLetter
#     print("Your decoded text is: ", cipherText)
#     return cipherText



#ANGELA SOLUTION
    #for letter in plain_text:
        #position = alphabet.index(letter)
        #new_position = position + shift_amount
        #new_letter = alphabet[new_position]
        #cipher_text += new_letter
    #print(f"The encoded text is: {}")

#encrypt(plain_text=text, shift_amount=shift)




#i need to understand this all, make comments.
if direction == "encode" or direction == "decode":
    caesar(plain_text = text, shift_amount = shift, the_direction = direction)
else:
    print("That was not an option")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 



#def caesar(start_text, shift_amount, cipher_direction):
    #end_text = ""
    #if cipher_direction == "decode":
        #new_position *= -1
    #for letter in start_text:
        #position = alphabet.index(letter)
        #new_position = position + shift_amount
        #end_text += alphabet[new_position]
        #print(f"The {cipher_direction}d text is {end_text}")

#caesar(start_text = text, shift_amount = shift, cipher_direction = direction)


#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 