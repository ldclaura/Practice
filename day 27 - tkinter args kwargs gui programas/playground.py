def add(*args):
    # print(args[2])
    sum = 0 
    for n in args:
        sum += n
    return sum
print(add(5, 6, 10))
 

# def calculate(**kwargs):#kwargs turns arguments to key value dictionary
#     print(kwargs) 
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#         print(kwargs["add"]) #gives value from key
def calculate(n, **kwargs):#kwargs turns arguments to key value dictionary
    print(kwargs)
    n += kwargs["add"] #2 + 3 = 5
    n *= kwargs["multiply"] #5 x 5 = 25
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"] #Nissan
        # self.model = kwargs["model"] #GT-R
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")
        #my_car = Car(make="Nissan") #keyerror if kwargs["model"] not specified.
# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan") #keyerror if kwargs["model"] not specified.
print(my_car.model) #keyerror if kwargs["model"] not specified. None if kwargs.get("model") not specified
print(my_car.make)