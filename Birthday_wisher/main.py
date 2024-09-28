import datetime as dt
import random
import smtplib



# 1. Updating the birthdays.csv

sender_email = "youremail@gmail.com"
with open("birthdays.csv", "r") as birthday_file:
    birthday = birthday_file.readlines()
    #print(birthday)
    for char in range(len(birthday)):
        if birthday[char] == "[Fill this in!]":
            birthday[char] =  f"Papa,yourpapaemail@gmail.com ,1973,9,19\n"
            birthday.append(f"Mummy,yourmummyemail@gmail.com ,1976,9,20\n")
            #print(birthday)
            updated_data = ''.join(birthday)
            print(updated_data)
            with open("birthdays.csv", "w") as birthday_file:
                birthday_file.write(updated_data)

# 2. Checking if today matches a birthday in the birthdays.csv
bday = dt.datetime.now()
birth_day = f"{bday.month},{bday.day}"
#print(birth_day)
birthday_available = False
with open("birthdays.csv") as birthdate_file:
    birthday = birthdate_file.readlines()

    for i in range(len(birthday)):
        check = birthday[i]
        if birth_day in check:
            check = check.split(",")
            print(f"Available, {check}")
            birthday_available = True

# 3. If step 2 is true, then picking a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

message = ""
if birthday_available:
    random_number = random.randint(1,3)

    file_path = f"letter_templates/letter_{random_number}.txt"
    with open(file_path, 'r') as name_file:
        name = name_file.readlines()
        #print(name)
        for i in range(len(name)):
            change = name[i]
            change = change.strip()
            if change == "Dear [NAME],":
                change = f"Dear {check[0]},"
            message += change + "\n"
print(message)



# 4. Sending the letter generated in step 3 to that person's email address.

my_email = "youremail@gmail.com"
password = "your password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="birthdaypersonemail@yahoo.com",
                        msg= f"Subject: Happy Birthday\n\n{message}")



