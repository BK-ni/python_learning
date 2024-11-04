import smtplib
import datetime as dt
import random


my_email = "nekodesuka777@gmail.com"
password = "vcbo huyr ryay dcxt"

now = dt.datetime.now()
weekday = now.weekday()
date = dt.datetime(year=2024, month=11, day=1)
print(date.weekday())
if weekday == date.weekday():
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="b0910688@yahoo.com.tw",
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )
