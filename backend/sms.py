import asyncio
from quart import session
from twilio_client import client
from app import messages_collection
from config import account_sid, auth_token


class OutgoingSMS:
   
    def __init__(self):
        self.admin_client = client
        self.user_client = client(account_sid, 
                            auth_token, 
                            session['sid'])


    async def send_sms(self, body, to):
      """A method to send an sms message.
      Args:
        self: an instance of the OutgoingSMS class
        body: string: 
        to: string: recepient sms number
      """
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


    def handle_sms_callback(self):
      """A method for parsing a callback from Twilio
      that is sent upon the receipt of a sms message.
      Args:
        self: an instance of the IncomingSMS class
      """
        data = {
          "recipient_sms_number": self.sms_object.to_number,
          "prompt": session['prompt'],
          "response": self.sms_object.body
        }
        self._write_to_db(data)


    def _write_to_db(self, data):
      """A method for writing an incoming sms message 
      to mongo.
      Args:
        self: an instance of the IncomingSMS class
        data: 
      """
        message_id = messages_collection.insert(data)
        return message_id

