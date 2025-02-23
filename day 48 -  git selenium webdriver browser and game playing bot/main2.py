from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys #select things

URL = "https://en.wikipedia.org/wiki/Main_Page"
URL2 = "https://secure-retreat-92358.herokuapp.com/"
#keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#---
driver = webdriver.Chrome(options=chrome_options) #webdriver.Firefox
#chrome with capital, initializing new object
#---


#find the english articles number
def english_articles_number():
    driver.get(URL)
    englisharticlesnumber = driver.find_element(By.CSS_SELECTOR, value="#articlecount > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    #presses the english articles number link
    englisharticlesnumber.click()
def content_portals():
    driver.get(URL)
    #find the content portals link
    all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
    #clicks content portals link
    all_portals.click()
def find_search():
    driver.get(URL)
    driver.maximize_window() #the search bar changes based on if the window is large or not. so it wont work unless max window
    #find search bar
    search = driver.find_element(By.NAME, value="search")
    search.send_keys("Python")
    search.send_keys(Keys.ENTER)
def signup():
    driver.get(URL2)
    first_name = driver.find_element(By.NAME, value="fName")
    last_name = driver.find_element(By.NAME, value="lName")
    email = driver.find_element(By.NAME, value="email")
    button = driver.find_element(By.CSS_SELECTOR, value="form button") #OR button = driver.find_element(By.CSS_SELECTOR, value=".btn")
    first_name.send_keys("John")
    last_name.send_keys("Doe")
    email.send_keys("JohnDoe@gmail.com")
    button.click()
    
signup()