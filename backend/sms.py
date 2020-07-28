import asyncio
from quart import session
from twilio_client import client
from app import users_collection
from config import account_sid, auth_token


class OutgoingSMS:
   
    def __init__(self):
        self.admin_client = client
        self.user_client = client(account_sid, 
                            auth_token, 
                            session['sid'])


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

class IncomingSMS:

    def __init__(self, sms_object):
        self.sms_object = sms_object


    def parse_sms_callback(self):
        pass


    def write_to_db(self):
        pass

