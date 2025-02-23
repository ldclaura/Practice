import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys #select things
import random
from selenium.common.exceptions import NoSuchElementException
RANDOM_SLEEP = [2, 3, 4]


EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")


class LinkedIn():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        #---
        self.driver = webdriver.Chrome(options=self.chrome_options) #webdriver.Firefox
        #chrome with capital, initializing new object
        self.driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4141990148&f_AL=true&keywords=python%20developer")
        self.driver.maximize_window()
        #---
    def login(self):
        """Selects login with email"""
        trying = True
        while trying:
            try:
                loginwithemail = self.driver.find_element(By.CSS_SELECTOR, value="#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button")
                time.sleep(random.choice(RANDOM_SLEEP))
                loginwithemail.click()
                trying = False
            except:
                time.sleep(random.choice(RANDOM_SLEEP))

    def inputlogindetails(self, email, password):
        """inputs email and password"""
        trying = True
        while trying:
            try:
                emailpassword = self.driver.find_element(By.CSS_SELECTOR, value="#base-sign-in-modal_session_password")
                time.sleep(random.choice(RANDOM_SLEEP))
                emailaddress = self.driver.find_element(By.CSS_SELECTOR, value="#base-sign-in-modal_session_key")
                time.sleep(random.choice(RANDOM_SLEEP))
                emailaddress.send_keys(email)
                time.sleep(random.choice(RANDOM_SLEEP))
                emailpassword.send_keys(password)
                time.sleep(random.choice(RANDOM_SLEEP))
                emailpassword.send_keys(Keys.ENTER)
            except:
                time.sleep(random.choice(RANDOM_SLEEP))

    def notrobot(self):
        """A function that doesn't work that is supposed to randomly select a verification image"""
        trying = True
        while trying:
            try:
                verifbutton = self.driver.find_element(By.CSS_SELECTOR, value="#home_children_button")
                randomdog = self.driver.find_element(By.CSS_SELECTOR, value=f"#image{str(random.choice(range(1, 6)))} > a")
                verifbutton.click()
                randomdog.click()

            #home_children_heading (h2)
            #home_children_button (button to press)
            #after press
            #game_children_text > h2 (pick the image that is the correct way up)
            #game_children_challenge > div > ul
            #image1 > a
            #image2 > a
            #image3 > a
            #image4 > a
            #image5 > a
            #image6 > a
            except:
                pass
    def save_job():
        pass
        #main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > div.mt4 > div > button
        #main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > div.mt4 > div > button > span.jobs-save-button__text
        #ember145
        #main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div > ul






#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button
link = LinkedIn()
link.login()
link.inputlogindetails(EMAIL, LINKEDIN_PASSWORD)
# link.notrobot()
#base-sign-in-modal_session_key