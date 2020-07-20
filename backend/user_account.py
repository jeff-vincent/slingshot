import subprocess
from twilio_client import client


class UserAccount:
    def __init__(self):
        pass

    def create_user_account(self, friendly_name):
        user_account = client.api.accounts.create(
            friendly_name=self.friendly_name)
        self._get_sms_number(user_account.sid)

    def _get_sms_number(self, user_sid):
        result = subprocess.call(
            'twilio phone-numbers:buy:mobile --country-code US --sms-enabled')
        # TODO: retrieve number from result
        new_phone_number = result
        self._assign_sms_to_user(new_phone_number, user_sid)

    def _assign_sms_to_user(self, new_phone_number, user_sid):
        client.incoming_phone_numbers(new_phone_number) \
            .update(account_sid=user_sid)
