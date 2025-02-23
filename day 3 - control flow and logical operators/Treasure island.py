#treasure island
print('''     |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("left or right?").lower()
if direction == "left":
    swim = input("You have arrived at a pool of water,\n did you want to swim or wait?").lower()
    if swim == "wait":
        door = input("You have arrived at a room of doors.\nWhich door will you take?\nRed, Blue, or Yellow?").lower()
        if door == "red":
            print("Burned by fire. Game over.")
        elif door == "yellow":
            print("You have found gold, you win!")
        elif door == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("You have been attacked by a trout.\nGame over.")
else:
    print("You fell into a hole. Game over.")