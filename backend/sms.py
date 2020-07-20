from twilio_client import client
from app import mongo
from config import account_sid, auth_token
from user_account import subaccount_sid


class SMS:
    def __init__(self):
        self.admin_client = client
        self.user_client = client(account_sid, 
                            auth_token, 
                            subaccount_sid)
        self.user_client_phone_number = self.user_client.

    def send_sms(self):
        message = self.user_client.messages.create(
                              from_='+14158141829',
                              body='Ahoy there!',
                              to='+16518675310'
                          )
