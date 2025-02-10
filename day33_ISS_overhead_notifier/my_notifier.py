import smtplib
MY_EMAIL = "example@gmail.com"
APP_PASSWORD = "<PASSWORD>"
SMTP_SERVER = "smtp.gmail.com"

def notify_me(subject = "Look up!",msg="ISS is above you in the sky."):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:{subject}\n\n{msg}"
        )