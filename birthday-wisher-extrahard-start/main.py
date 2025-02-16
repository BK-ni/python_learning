##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random


# 1. Update the birthdays.csv
my_email = "nekodesuka777@gmail.com"
password = "vcbo huyr ryay dcxt"

data = pandas.read_csv("birthdays.csv")
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
# 2. Check if today matches a birthday in the birthdays.csv
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject: Happy Birthday!\n\n{contents}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




