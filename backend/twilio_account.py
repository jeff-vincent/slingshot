import asyncio
import subprocess
from quart import session
from twilio_client import client
from async_http import AsyncHTTP
from config import twilio_current_sms_numbers_base_uri
from config import twilio_purchase_sms_number_base_uri


class CreateTwilioAccount:
    
    def __init__(self, friendly_name):
        self.friendly_name = friendly_name
        self.async_http = AsyncHTTP()


    async def create_user_account(self):
        user_account = await client.api.accounts.create(
            friendly_name=self.friendly_name)
        
        user_sid = user_account.sid
        sms_number = await self._get_available_sms_number(user_sid)
        return {'sms_number':sms_number, 'sid': user_sid}


    async def _get_available_sms_number(self, user_sid):
        params = { 
            'area_code'=session['area_code'],
            'sms_enabled'=True, 
            'user_sid'=user_sid}

        response = await self.async_http.post(
            base_uri=twilio_current_sms_numbers_base_uri,
            params=params)

        sms_number = response.available_numbers[0]
        response = await self._purchase_sms_number(user_sid, sms_number)
        return response


    async def _purchase_sms_number(self, user_sid, sms_number):
        response = await self.async_http.post(
            base_uri=twilio_purchase_sms_number_base_uri, 
            sms_number=sms_number,
            user_sid=user_sid)
        response = await self._assign_sms_number_to_user(user_sid, sms_number)
        return response


    async def _assign_sms_number_to_user(self, user_sid, sms_number):
        response = await client.incoming_phone_numbers(sms_number) \
            .update(account_sid=user_sid)
        return response
