from quart import session
from twilio_client import client
from app import users_collection
from config import account_sid, auth_token
from twilio_account import subaccount_sid


class SMS:
   
    def __init__(self):
        self.admin_client = client
        self.user_client = client(account_sid, 
                            auth_token, 
                            subaccount_sid)


    async def send_sms(self, body, to):
        try:
            message = await self.user_client.messages.create(
                                  from_= session['sms_number'],
                                  body=body,
                                  to=to
                              )
            return 'message sent'
        except:
            return 'message failed'

