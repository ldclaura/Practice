import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib
# import dotenv
# from dotenv import load_dotenv

URL = "https://appbrewery.github.io/instant_pot/" #udemy URL
URL2 = "https://www.amazon.com/Surround-Headphones-Cancelling-Flexible-Earmuffs/dp/B09TB15CTL/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.KLIcXRVVXpsHzp-MC1Bc-zMY1Cu7ITOQlCvvtU7eYRhDBX5lc75zspP03vKWLKpRRlEp8B7-zeO1hrveG_yQQx-jLe1ZSnbhSAtd6RBr9so-7dQXs0QZoeLVLKJmvQ4uPPg2DZOlGujV4wZeZl1SeUl4YU_XNUZ0sn3DnOz7U6pVaVS4DJ-I0hqr1ADJAUaiHUzaEk53_YficDsUl5PYNzn96DdViZMj4UtprPnMgIo.dLyToJHrMnekSEgj6quex1EiMnpRS66MaXdeIoLrNTg&dib_tag=se&keywords=gaming%2Bheadsets&pd_rd_r=235c81fe-94eb-4103-abe5-8ef55c3e3870&pd_rd_w=AWTAu&pd_rd_wg=qleLs&qid=1738202114&sr=8-1&th=1"
URLAUS = "https://www.amazon.com.au/Ikigai-Japanese-secret-long-happy/dp/178633089X/ref=cm_gf_aAN_d_p0_e0_qd0_dS9wJ2Ax3sVUQdXaejl0?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D"
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

#some headphones from actual amazon ^

def find_item_url():
    """Search for item, finds item on amazon, returns url for item"""
    pass

def scrape_product_price(url):
    """Scrapes product based on URL, finds the current price, returns current price"""
    response = requests.get(url, headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0", "Accept-Language" : "en-US"})
    print(response)
    top_songs_page = response.text
    soup = BeautifulSoup(top_songs_page, 'html.parser')
    price = soup.find(class_="a-price-whole")
    fraction = soup.find(class_="a-price-fraction")
    price = price.contents
    fraction = fraction.contents
    theprice = float(price[0]+"."+fraction[0])
    return theprice
    #NOTE: does not work with amazon australia must be international amazon
    #NOTE: for some reason the URL2 price number is wrong and i don't know why
    #i tried finding where the number came from and i couldn't find anything
    #other links work though


def email_alert(cost):
    """Sends email alert of current price of item"""
    try:  
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="lauracain12345@gmail.com", msg=f"""Subject:Amazon Price Tracker\n
    Your item is ${cost} dollars""")
    except:
        print(f"Failed to send")
    finally:
        print("COMPLETED")

userinput = input("Did you want to find the price of an item and send you an email of the price? Y/N").upper()
if userinput == "Y":
    price = scrape_product_price(URL2)
    print(f"${price}")
    email_alert(price)
else:
    "nothing was done"

