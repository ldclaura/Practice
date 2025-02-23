from selenium import webdriver
from selenium.webdriver.common.by import By


#keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#---
driver = webdriver.Chrome(options=chrome_options) #webdriver.Firefox
#chrome with capital, initializing new object
#---

URL = "https://www.amazon.com/Surround-Headphones-Cancelling-Flexible-Earmuffs/dp/B09TB15CTL/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.KLIcXRVVXpsHzp-MC1Bc-zMY1Cu7ITOQlCvvtU7eYRhDBX5lc75zspP03vKWLKpRRlEp8B7-zeO1hrveG_yQQx-jLe1ZSnbhSAtd6RBr9so-7dQXs0QZoeLVLKJmvQ4uPPg2DZOlGujV4wZeZl1SeUl4YU_XNUZ0sn3DnOz7U6pVaVS4DJ-I0hqr1ADJAUaiHUzaEk53_YficDsUl5PYNzn96DdViZMj4UtprPnMgIo.dLyToJHrMnekSEgj6quex1EiMnpRS66MaXdeIoLrNTg&dib_tag=se&keywords=gaming%2Bheadsets&pd_rd_r=235c81fe-94eb-4103-abe5-8ef55c3e3870&pd_rd_w=AWTAu&pd_rd_wg=qleLs&qid=1738202114&sr=8-1&th=1"
URL2 = "https://www.python.org/"
URL3 = "https://en.wikipedia.org/wiki/Main_Page"
#open chrome


#URL
def amazon_price():
    price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
    price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
    print(f"the price is: {price_dollar}.{price_cents}")
    driver.quit() #closes all tabs

#URL2
def python_site_input():
    search_bar = driver.find_element(By.NAME, value="q") #no .text prints as selenium element
    print(search_bar) #prints as selenium element
    print(search_bar.get_attribute("placeholder"))
    button = driver.find_element(By.ID, value="submit")
    print(button.size) #{'height': 40, 'width': 46}
    documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    print(documentation_link.text) #docs.python.org
    submit_bug = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a') #inspect page, right click, copy by xpath.

    #/html/body/div/footer/div[2]/div/ul/li[3]/a - what i got when i copied xpath
    #//*[@id="site-map"]/div[2]/div/ul/li[3]/a - what yu got when she copied xpath
    #they both work
    #copy xpath vs copy full xpath, firefox doesn't have 'full' option differentiated, so i assume the yu one is the shortened and mine is full
    #i used firefox she used chrome

    print(submit_bug.text)
    # driver.find_elements(By.CSS_SELECTOR, value="") #find multiple elements
    driver.quit() #closes all tabs
def upcoming_events():
    events_title = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/div[2]/div/h2")
    event = driver.find_element(By.CSS_SELECTOR, value=".event-widget > div:nth-child(1) > ul:nth-child(3)") #css_selector of list
    print(events_title.text)

    print("----------------------")
    # lines = event.text.split("\n")
    # events_dates = {lines[::2]:lines[1::2] for line in lines}
    #idk if this works ^

    lines = event.text.split("\n")
    # dates = lines[::2]  # Even-indexed elements (dates)
    # events = lines[1::2]  # Odd-indexed elements (event names)
    # events_dates = dict(zip(dates, events))

    events_dates = {lines[i]:lines[i+1] for i in range(0, len(lines), 2)} #range(start,stop,step)
    #this don work either V

    # num_events_dates = {}
    # for n in range(1, len(lines)):
    #     num_events_dates[n] = {
    #         "time": lines[n],
    #         "name": lines[n]
    #     }
    # print(num_events_dates)

    
    # for n in range(1, len(lines)):
    #     events_dates = {n:{lines[i]:lines[i+1]} for i in range(0, len(lines), 2)}
    #basically it loops through every item, so the start changes depending on the item.
    #so the step will always be the next item.
    #---
    #THIS SHIT DON WORK
    # num_events_dates = {}
    # for key, value in events_dates.items():
    #     new_value = {key, value}
    #     print(key, value)
    #     num_key = 1
    #     num_events_dates.update({num_key:new_value})
    #     num_key += 1
        

    # print(num_events_dates)
    #---


    print(events_dates)
    driver.quit()
def wikipedia():
    englisharticles = driver.find_element(By.CSS_SELECTOR, value="#articlecount > ul:nth-child(1) > li:nth-child(2)") #css_selector of list
    englisharticlesnumber = driver.find_element(By.CSS_SELECTOR, value="#articlecount > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)")
    #articlecount > ul:nth-child(1) > li:nth-child(2)
    print(englisharticlesnumber.text)
    englisharticlesnumber.click()
    driver.quit()


#open chrome
try:
    driver.get(URL3)
    
    wikipedia()
    print("done")

except:
    print("no")
# <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

# driver.close() #closes active tab, closes single tab
# driver.quit() #closes all tabs





