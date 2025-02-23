import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top_movies_page = response.text
soup = BeautifulSoup(top_movies_page, 'html.parser')
movies = soup.find_all(name="h3", class_="title")
# print(articles)
list_of_movies = []

for movie in movies:
    text = movie.getText()
    list_of_movies.append(text)
print(list_of_movies)

with open("./Starting Code - 100 movies to watch start/movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed(list_of_movies):
        file.write(f"{movie}\n")
    #if file doesn't already exist, it will create one.
