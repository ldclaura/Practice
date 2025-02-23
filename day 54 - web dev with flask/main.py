import time

def delay_decorator(function):
    """def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function"""
    def wrapper_function():
        time.sleep(2) #<-- do something before function
        function()
        #function() <-- run func twice
        #do something after function
    return wrapper_function


#all of the functions with the @delay_decorator will be delayed by time.sleep(2)
@delay_decorator
def say_hello():
    # time.sleep(2)
    print("Hello")
@delay_decorator
def say_bye():
    # time.sleep(2)
    print("Bye")
def say_greeting():
    # time.sleep(2)
    print("Greeting")

#this works the same as @delay_decorator but @delay_decorator is easier to read
decorated_function = delay_decorator(say_greeting)
decorated_function()

say_hello()
say_bye()
say_greeting()