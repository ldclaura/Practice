#spreadsheet of birthdays
#email smtp
#datetime
#gmail app password : 



# 4. By default smtplib.SMTP uses port 25. This used to be the standard SMTP port, but because of abuse in the past most servers nowadays have blocked this port to external traffic. There are still some that do allow it; Hotmail, Live, etc. Port 25 is still used for traffic between servers, but many providers have switched to using port 587 for external traffic. If in doubt, search the internet for "smtp server settings" for your provider.

# Add a port number by changing your code to this:

# smtplib.SMTP("smtp.gmail.com", port=587) 

#how email works

#sender - recipient
#gmail mail server receives your message
#yahoo mail server stores message
#timmy downloads from yahoo mail server
#smtp = simple mail transfer protocol
#mail server = postoffice
#smtp is postman


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
if year == 2024:
    print("2024 yay")
print(type(year))
print(type(now))
print(year)
print(month)
print(now)

date_of_birth = dt.datetime(year=2004, month=9, day=7, hour=1, minute=2, second=3)
print(date_of_birth)








# import smtplib

# with smtplib.SMTP("smtp.gmail.com") as connection: #with as closes it automatically
#     # connection = smtplib.SMTP("smtp.gmail.com")
#     #tls = transport layer security
#     connection.starttls() #encrypted if someone tries to get in?
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="2345@gmail.com", msg="""Subject:Hello\n\n
#     This is the body of my email""")




    # connection.close()