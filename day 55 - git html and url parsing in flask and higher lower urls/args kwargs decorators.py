class User():
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticated_decorator(function): #function is create_blog_post
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True: #if User("Laura") is logged in
            function(args[0]) #function(args[0]) represents create_blog_post(new_user)
        else:
            pass
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

new_user = User("Laura")
create_blog_post(new_user)

# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper

def yu_logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

# TODO: Use the decorator 👇
print("My solution being used:")
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)

print("Yu's solution:")
@yu_logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)