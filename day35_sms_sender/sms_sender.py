from twilio.rest import Client
import os
from dotenv import load_dotenv,find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_TWILIO_NUMBER = os.getenv("MY_TWILIO_NUMBER")

RECEIVER_NUMBER = os.getenv("RECEIVER_NUMBER")
print(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_=MY_TWILIO_NUMBER,
        body="Don't forget your umbrella!",
        to=RECEIVER_NUMBER
    )
