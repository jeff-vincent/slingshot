import asyncio
import subprocess
from quart import session
from async_http import AsyncHTTP
from config import twilio_available_sms_numbers_base_uri
from config import twilio_purchase_sms_number_base_uri
from config import auth_token


class CreateTwilioAccount:
    
    def __init__(self, friendly_name):
        self.friendly_name = friendly_name
        self.async_http = AsyncHTTP()


    async def create_user_account(self):
        """A method for creating a system user account.
        Args:
            self: an instance of the CreateTwilioAccount class
        """
        # probably blocking call via sdk
        user_account = await client.api.accounts.create(
            friendly_name=self.friendly_name)
        
        user_sid = user_account.sid
        signed_up_user = await self._get_sms_user(user_sid)
        return signed_up_user


    async def _get_sms_user(self, user_sid):
        """A private method for getting a list of available,
        sms-enabled phone numbers in a given area code. Calls
        private helper methods to complete the process of 
        purchasing a number from the list, and assigning 
        it to the Twilio subaccount.
        NOTE: the area code is set on the session.
        Args:
            self: an instance of the CreateTwilioAccount class
            user_sid: string
        """
        request_uri = twilio_available_sms_numbers_base_uri.format(
            auth_token=auth_token)

        response = await self.async_http.get(base_uri=request_uri)

        sms_number = response.available_phone_numbers[0].friendly_name
        response = await self._purchase_sms_number(user_sid, sms_number)
        return response


    async def _purchase_sms_number(self, user_sid, sms_number):
        """A private method for purchasing a given sms-enabled number.
        Args:
            self: an instance of the CreateTwilioAccount class
            user_sid: string
            sms_number: string: the sms number to buy
        """
        params = {'phone_number':sms_number}
        request_uri = twilio_purchase_sms_number_base_uri.format(
            auth_token=auth_token)
        response = await self.async_http.post(
            base_uri=request_uri, 
            params=params)
        response = await self._assign_sms_number_to_user(user_sid, sms_number)
        return response


    async def _assign_sms_number_to_user(self, user_sid, sms_number):
        """A private method for assigning a sms-enabled number 
        to a Twilio subaccount.
        Args:
            self: an instance of the CreateTwilioAccount class
            user_sid: string
            sms_number: string: the number that was just purchased.
        """
        response = await client.incoming_phone_numbers(sms_number) \
            .update(account_sid=user_sid)
        return response
