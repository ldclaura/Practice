#tip calculator
print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?")
split = input("How many people to split the bill?")

inttotal = int(total)
inttip = int(tip)
intsplit = int(split)

tiptotal = inttip / 100
tiptotal2 = inttotal * tiptotal

finaltotal = int(inttotal) + int(tiptotal2)
billperperson = finaltotal / intsplit
answer = round(billperperson, 2)
print(f"Each person should pay: ${answer}")