import random
import smtplib

import pandas
import datetime as dt
import numpy as np

LETTER_TEMPLATES = 3

MY_EMAIL = "example@gmail.com"
APP_PASSWORD = "<PASSWORD>"
SMTP_SERVER = "smtp.gmail.com"


def random_letter_template():
    letter_index = random.randint(1, LETTER_TEMPLATES)
    with open(f"letter_templates/letter_{letter_index}.txt") as f:
        content = f.read()
        return content


def generate_letter(receiver_name):
    template_content = random_letter_template()
    return template_content.replace("[NAME]", receiver_name)


print(random_letter_template())

df = pandas.read_csv('birthdays.csv')

today = dt.datetime.today()
today_birthday = df[np.logical_and(df['month'] == today.month, df['day'] == today.day)]

for _, row in today_birthday.iterrows():
    name = row['name']
    email = row['email']
    letter_content = generate_letter(name)
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )
