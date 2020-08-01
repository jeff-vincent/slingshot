import asyncio
import datetime
from quart import session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


from twilio_account import CreateTwilioAccount


class UserManagement:

    def __init__(self, request, users_collection):
        self.request = request
        self.users_collection = users_collection


    async def get_user(self, username):
        user = await self.users_collection.find_one(
            {'username': username})


    async def _parse_sign_up_request(self):
        request_data = {}
        request_data['form'] = await self.request.form
        request_data['username'] = await form.get('username')
        request_data['password'] = await form.get('password')
        request_data['payment_type'] = await form.get('payment_type')
        request_data['cc_number'] = await form.get('cc_number')
        request_data['area_code'] = await form.get('area_code')
        return request_data


    async def _strip_sensitive_fields(self, request_data):
        request_data['payment_type'] = None
        request_data['password'] = None
        request_data['cc_number'] = None
        request_data['area_code'] = None
        request_data['sid'] = None
        return request_data


    async def _augment_sign_up_data(self, request_data, twilio_user):
        hashed_password = await generate_password_hash(request_data['password'])
        request_data['password'] = hashed_password  
        request_data['date_joined']: datetime.datetime.utcnow(),
        request_data['sms_number']: twilio_user['sms_number'],
        request_data['sid']: twilio_user['sid'], 


    async def signup(self):
        """ A method for signing up for the service."""
        # parse the request
        try:
            request_data = await self._parse_sign_up_request()
        except Exception as e:
            return 'There was a problem parsing your request.\
             Error message: {}'.format(str(e))

        # check that user namespace is available
        user = await self.get_user(request_data['username'])
        if user:
            return 'Sorry, but that username is already taken.\
             Please choose a different username.'

        # attempt to associate user with Twilio subaccount
        twilio = CreateTwilioAccount(area_code=area_code,friendly_name=username)
        try:
            twilio_user = await twilio.create_user_account()
        except:
            return 'Twilio error'

        # create user
        request_data = self._augment_sign_up_data(request_data)
        user_id = await self.users_collection.insert(request_data)
        data = await self._strip_sensitive_fields(request_data)
        return jsonify(data)


    async def login(self):
        try:
            form = await self.request.form
            username = await form.get('username')
            password = await form.get('password')
        except Exception as e:
            return 'There was a problem parsing your request.\
             Error message: {}'.format(str(e))

        try:
            user = await self.get_user(username)
            
            if check_password_hash(user['password'],  password):
                session['sms_number'] = user['sms_number']
                session['sid'] = user['sid']
                return 'Logged in user: {}'.format(user['username'])
            
            return 'Please log in.'
        except Exception as e:
            return 'Login failed: ' + (str(e))


    async def recover_password(self):
        pass
