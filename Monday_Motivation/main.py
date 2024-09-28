import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

# date_of_birth = dt.datetime(year=1998, month=7, day=17, hour=6)
# print(date_of_birth)
with open("quotes.txt", "r") as quote_file:
    quote = quote_file.readlines()
    random_quote = random.randint(0,len(quote))
    quote_text = quote[random_quote]
    print(quote_text)

my_email = "youremail@gmail.com"
password = "yourpassword"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="anotheremail@yahoo.com",
                        msg= f"Subject: Monday Motivation\n\n{quote_text}")

