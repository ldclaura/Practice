##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



#make sure all birthdays are in txt files
#watch python 100 days: 250. Run Your Python Code in the Cloud!


#go into files top right
#upload files, make new directory for folder

import smtplib, datetime as dt, random, pandas, os
my_email = "54@gmail.com"
password = "i "
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
birthdays = pandas.read_csv("birthdays.csv")

def send_birthday_email(name, email):
    with open(f"letter_templates\{random.choice(letters)}", "r") as file:
        file_contents = file.read()
        updated_contents = file_contents.replace("[NAME]", name)
        print(updated_contents)
    try:  
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"""Subject:Happy Birthday :)\n
{updated_contents}""")
    except:
        print(f"Failed to send to {name}")
    finally:
        print("COMPLETED")


def thisday():
    now = dt.datetime.now()
    thismonth = now.month
    thisdate = now.day
    birthdaytoday = birthdays[(birthdays.month == thismonth) & (birthdays.day == thisdate)]
    for (index, row) in birthdaytoday.iterrows():
        print(row["name"])
        print(row["email"])
        print(row["year"])
        print(row["month"])
        print(row["day"])
        send_birthday_email(row["name"], row["email"])
    

thisday()


