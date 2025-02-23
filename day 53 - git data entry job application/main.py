import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys #select things
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException

#-----------------------------------------------------------
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
#---------------------------------------
import re
#perhaps try https://www.zenrows.com/blog/undetected-chromedriver#scrape-data-using-undetected-chromedriver
#undetected chromedriver???

# self.browser.maximize_window()
# wait = WebDriverWait(self.browser, 30)
# self.browser.get('https://www.twitter.com/login')

# username_input = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
# username_input.send_keys('send username here')
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")
TWITTER_NAME = os.getenv("TWITTER_NAME")


URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLEFORMURL = "https://forms.gle/"
#all places you can rent in sanfran up to 300 dollars a month, one bedroom
#zillow
#price, address, url link to actual listing
#selenium to autofill google form.
#google form to spreadsheet

#TODO:
#create google form manually
#short answer - 'whats the address of the property?', 'whats the price per month?', 'what's the link to the property?'
#Click send and copy the link address of the form. You will need to use this in your program.
#Go to https://appbrewery.github.io/Zillow-Clone/ and see how the website is structured. This is where you'll be scraping the data from:
#Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address (Step 4 above).
# Create a list of links for all the listings you scraped. e.g.
class ZillowScrape():
    def __init__(self):
        self.response = requests.get(URL)
        self.zillow_webpage = self.response.text
        self.soup = BeautifulSoup(self.zillow_webpage, 'html.parser')
        self.addressprice = []
        self.address = []
        self.addresslink = []

    def findlinks(self):
        findapartments = self.soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        for item in findapartments:
            address = item.find(name="address")
            cleanedaddress = address.text.replace("\n", "")
            cleanedaddress = re.sub('\s{2,}', ' ', cleanedaddress)
            cleanedaddress = cleanedaddress [1:-1]
            #^ fix up, remove spaces and /n
            link = item.find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href")
            price = item.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
            # print(link)
            # print(address.text)
            # print(price.text)
            self.addressprice.append(price.text)
            self.address.append(cleanedaddress)
            self.addresslink.append(link)
        # print(self.address)
        # print(self.addressprice)
        # print(self.addresslink)
        # print(type(self.address[0]))
        # print(type(self.addressprice[0]))
        # print(type(self.addresslink[0]))
        #     text = item.getText()
        #     apartments.append(text)
        #     print(apartments)
        # print(text)



        # article_texts = []
        # article_links = []
        # for article_tag in articles:
        #     text = article_tag.getText()
        #     article_texts.append(text)
        #     link = article_tag.find(name='a').get("href")
        #     article_links.append(link)
    def returnaddressprice(self):
        return self.addressprice
    def returnaddress(self):
        return self.address
    def returnaddresslink(self):
        return self.addresslink

class DataEnterer():
    """opens google form and fills it out"""
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        #---
        self.driver = webdriver.Chrome(options=self.chrome_options) #webdriver.Firefox
        #chrome with capital, initializing new object
        self.driver.get(GOOGLEFORMURL)
        self.driver.maximize_window()
        #---

    def autofill_propertys(self, price, addr, link):
        """Use Selenium to fill in the form you created (step 1,2,3 above).
          Each listing should have its price/address/link added to the form.
            You will need to fill in a new form for each new listing. e.g.
            Once all the data has been filled in,
              click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form.
              You should end up with a spreadsheet with all the details from the properties.
              """
        for _ in range(len(addr)):
            straddr = addr[_]
            strlink = link[_]
            strprice = price[_]

        #addr
            inputaddress = self.driver.find_element(By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            inputaddress.send_keys(straddr)

            priceinput = self.driver.find_element(By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            priceinput.send_keys(strprice)
        #mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input

            linkinput = self.driver.find_element(By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            linkinput.send_keys(strlink)

            button = self.driver.find_element(By.CSS_SELECTOR, value="#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div")
            button.click()
            submitanotherform = self.driver.find_element(By.CSS_SELECTOR, value=".c2gzEf > a:nth-child(1)")
            submitanotherform.click()
            time.sleep(2)
        #mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input
        # for _ in price:
        #     pass
    def troubleshoot(self):
        print(webdriver.Chrome().capabilities['browserVersion'])
        print(webdriver.Chrome().capabilities['chrome']['chromedriverVersion'].split(' ')[0])

#spreadsheet should have
#timestamp (date of data collection) | whats the address of the property? | whats the price per month | what sthe link to the property? | 
#2/14/2025 12:59:10                  | 15 sullivans rd strath             | 100                       | www.google.com
scrapezillow = ZillowScrape()
scrapezillow.findlinks()
globaladdressprice = scrapezillow.returnaddressprice()
globaladdress = scrapezillow.returnaddress()
globaladdresslink = scrapezillow.returnaddresslink()
print(globaladdresslink)
dataentry = DataEnterer()
dataentry.troubleshoot() #for some fuckin reason it doesn't work unless i run this function i made that was supposed to explain why it doesn't work lol
#it just suddenly started work when i used this func
#so ill keep it here

dataentry.autofill_propertys(globaladdressprice, globaladdress, globaladdresslink)
#2 extra tabs open. i dont know why. but the program works anyway. so its not important


