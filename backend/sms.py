import asyncio
from quart import session
from app import messages_collection
from config import account_sid, auth_token
from config import twilio_send_sms_base_uri
from async_http import AsyncHTTP


class OutgoingSMS:
   
    def __init__(self):
        self.async_http = AsyncHTTP()


    async def send_sms(self, body, to):
      """A method to send an sms message.
      Args:
        self: an instance of the OutgoingSMS class
        body: string: 
        to: string: recepient sms number
      """
        request_uri = twilio_send_sms_base_uri.format(
          auth_token=auth_token)

        params = {
          'from':session['sms_number'],
          'body':body,
          'to':to
          }

        try:
            message = await self.async_http.post(
                                  base_uri=request_uri,
                                  params=params)
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

