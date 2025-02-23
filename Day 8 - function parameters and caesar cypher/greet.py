#Review:
# Create a function called greet()
# Write 3 print statements inside the function. 
# Call the greet() and run your code

def greet():
    print("Hello")
    print("Hallo")
    print("Bonjour")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hallo {name}")
    print(f"Bonjour {name}")

greet_with_name("Laura")

# name = parameter and "Laura" = argument

#argument is actual value of data, parameter is name of data.

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location="location", name="Laura") #keyword arguments