from bs4 import BeautifulSoup
import requests
link = "https://news.ycombinator.com/news"
response = requests.get(link)
yc_website = response.text


soup = BeautifulSoup(yc_website, "html.parser")
print(soup.title)


article_tag = soup.find(class_="titleline")
print(article_tag.getText())

#find article_link and article_upvote
article_link = soup.find(class_="sitestr")
article_rank = soup.find(class_="rank")
article_upvote = soup.find(class_="score")
print(article_link.getText())
print(article_upvote.getText())



















# with open("./bs4-start/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser") #"lxml", import lxml
# print(soup.title)
# print(soup.title.string)

# all_anchor_tags = soup.find_all(name="a")
# all_paragraph_tags = soup.find_all(name="p")
# print(all_anchor_tags)


# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))


# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)