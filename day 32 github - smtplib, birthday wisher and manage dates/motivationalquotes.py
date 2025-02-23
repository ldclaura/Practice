import smtplib, datetime as dt, random
my_email = "gmail54@gmail.com"
password = "password "

def random_quote():
    with open("quotes.txt", "r") as file:
        lines = file.readlines()
        random_num = random.randint(0,len(lines))
        return lines[random_num]

randomquote = random_quote()

def send_motivational_email(quote):
    now = dt.datetime.now()
    day_of_week = now.weekday()
    if day_of_week == 0:
        with smtplib.SMTP("smtp.gmail.com") as connection: #with as closes it automatically
            # connection = smtplib.SMTP("smtp.gmail.com")
            #tls = transport layer security
            connection.starttls() #encrypted if someone tries to get in?
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="gmail@gmail.com", msg=f"""Subject:Monday Motivation :)\n\n
            {quote}""")
    else:
        pass
send_motivational_email(randomquote)

    #looks at current date and time and emails motivational quote on certain days