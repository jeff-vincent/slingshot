import subprocess
from twilio_client import client


class CreateTwilioAccount:
    
    def __init__(self, friendly_name):
        self.friendly_name = friendly_name


    async def create_user_account(self):
        user_account = await client.api.accounts.create(
            friendly_name=self.friendly_name)
        
        user_sid = user_account.sid
        sms_number = await self._get_sms_number(user_sid)
        return sms_number


    async def _get_sms_number(self, user_sid):
        result = await subprocess.call(
            'twilio phone-numbers:buy:mobile --country-code US --sms-enabled')
        # TODO: retrieve number from result
        sms_number = result.sms_number
        self._assign_sms_to_user(sms_number, user_sid)
        return sms_number


    async def _assign_sms_to_user(self, new_phone_number, user_sid):
        await client.incoming_phone_numbers(sms_number) \
            .update(account_sid=user_sid)
