#classes and object oriented programming

class User: #capitalized name (pascal case)
    """what the users have and what they do"""
    
#CONSTRUCTORS
#initializing an object
#__init__ function
#
    def __init__(self, id, username):
        """ user_1 = User()
        
        user_1.id = "001"

        user_1.username = "laura"

        #create attribute for class

        print(user_1.username)


        user_2 = User()

        user_2.id = "002"

        user_1.username = "joe"

        print(user_1.id)"""
        print("New user being created...") #this prints everytime user is created.
        self.id = id
        self.username = username
        self.followers = 0 #not a parameter, do not need to input, all users will be default 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
user_1 = User("001", "laura")
user_2 = User("002", "joe")
print(user_1.username)
print(user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#when a function is attached to a class it's called a method



# user_1 = User()
# user_1.id = "001"
# user_1.username = "laura"
# #create attribute for class
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_1.username = "joe"
# print(user_1.id)

