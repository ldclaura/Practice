#try
#something that might fuck up, prob will work maybe not

#except
#if something goes wrong do this

#else
#if no exception

#finally
#no matter what happens it does this
# """try:
#     file = open("a_file.txt")
# except FileNotFoundError:
# #except: #too broad exception clause ignores errors
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     print("AAH")
# finally:
#     raise KeyError("You are retarded") (makes keyerror)
#     file.close()
#     print("File closed")"""

#----------------------------------------------------------------------------------------
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            post['Likes'] = 0
            total_likes = total_likes + post['Likes']
    
    return total_likes


print(count_likes(facebook_posts))