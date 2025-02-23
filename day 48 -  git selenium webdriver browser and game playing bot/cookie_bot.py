# #langSelect-EN

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys #select things
URL = "https://orteil.dashnet.org/cookieclicker/"
class CookieBot():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        #---
        self.driver = webdriver.Chrome(options=self.chrome_options) #webdriver.Firefox
        #chrome with capital, initializing new object
        self.driver.get(URL)
        self.driver.maximize_window()
        self.bigcookie = self.driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
        #---
    def start(self):
        """Selects language so game can start"""
        trying = True
        while trying:
            try:
                selectlang = self.driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
                selectlang.click()
                trying = False
            except:
                pass

    def press_cookie(self):
        """Presses and returns amount of cookies"""
        self.bigcookie = self.driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
        self.bigcookie.click()
        cookies = self.driver.find_element(By.CSS_SELECTOR, value="#cookies")
        cookies = [int(s) for s in cookies.text.split() if s.isdigit()]
        return cookies[0]
    def store_purchase(self, cookies, product, productprice):
        grandma = self.driver.find_element(By.CSS_SELECTOR, value=product)
        grandmaprice = self.driver.find_element(By.CSS_SELECTOR, value=productprice)
        if cookies == int(grandmaprice.text):
            print(grandmaprice.text)
            grandma.click()

window = CookieBot() #create variable with class otherwise it will open new windows.
window.start()
gameison = True

while gameison:
    try:
        #turns to 6 when goes past 1,000
        #also stops upgrading after 2 upgrades? can work with assistance
        #might be too quick.
        cook = window.press_cookie()
        if cook >= 20000000:
            window.store_purchase(cook, "#product6", "#productPrice6")
        if cook >= 1400000:
            window.store_purchase(cook, "#product5", "#productPrice5")
        if cook >= 130000:
            window.store_purchase(cook, "#product4", "#productPrice4")
        if cook >= 13800:
            window.store_purchase(cook, "#product3", "#productPrice3")
        if cook >= 1673:
            window.store_purchase(cook, "#product2", "#productPrice2")
        if cook >= 100:
                window.store_purchase(cook, "#product1", "#productPrice1")
        print(cook)
    except:
        pass
            # cookie = self.driver.find_element(By.CSS_SELECTOR, value="#cookies")
        # print(cookie.text)
#146 cookies
#per second: 0