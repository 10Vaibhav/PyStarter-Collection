import datetime as dt
import os
import random
import smtplib
import pandas as pd

my_email = "vaibhavmahajan43810@gmail.com"
password = "pckaebvnhtqeshjt"

data = pd.read_csv("birthdays.csv")

names = data.name.to_list()
months = data.month.to_list()
day = data.day.to_list()
emails = data.email.to_list()

tuples = [(months[i], day[i]) for i in range(len(months))]

random_file = random.choice(os.listdir("./letter_templates"))


birthdays_dict = {}
mail_dict = {}
for i in range(len(tuples)):
    with open(f"./letter_templates/{random_file}", "r") as file:
        letter_content = file.read()
        new_letter = letter_content.replace("[NAME]", names[i])
    birthdays_dict[tuples[i]] = new_letter
    mail_dict[tuples[i]] = emails[i]

current = dt.datetime.now()
today_month = current.month
today_day = current.day

if (today_month, today_day) in birthdays_dict:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=mail_dict[(today_month, today_day)],
                            msg=birthdays_dict[(today_month, today_day)])


