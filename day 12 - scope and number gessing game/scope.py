################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope exists within funcs
#only valid within functions

#global scope
#created outside function

#concept called namespace

#when creating variable you need to be aware of where you created it

#there is no block scope, if statements ect, local variables are created in functions not ifs



def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function 2: {enemies}")
#cannot modify global scope,
#u dont want to because its confusing doe
#do not modify global scope

increase_enemies()
print(f"enemies outside function after changed by increase enemies: {enemies}")


#do this instead of globalising a variable
def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


#global constants
#variables defined that u never plan on changing
PI = 3.14159
#^ use uppercase to show u will never change it

