import asyncio
import datetime
from quart import request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from twilio_account import CreateTwilioAccount
from db.db_connector import MotorQuery

class UserManagement:

    def __init__(self, request, users_collection):
        self.request = request
        self.users_collection = users_collection
        self.motor_query = MotorQuery()
        self.get_user = self.motor_query.get_user()


    # async def get_user(self, username):
    #     """A method for getting a user record by username.
    #     Args:
    #         self: an instance of the UserManagement class
    #         username: string
    #     """
    #     user = await self.users_collection.find_one({'username': username})
    #     return user


    async def _parse_sign_up_request(self):
        """A method for parsing sign up requests. 
        Args:
            self: an instance of the UserManagement class
        """
        request_data = {}
        form = await self.request.form
        request_data['username'] = await form.get('username')
        request_data['password'] = await form.get('password')
        request_data['payment_type'] = await form.get('payment_type')
        request_data['cc_number'] = await form.get('cc_number')
        request_data['area_code'] = await form.get('area_code')
        # set area code to session for Twilio account creation
        session['area_code'] = request_data['area_code']
        return request_data


    async def _strip_sensitive_fields(self, request_data):
        """A method for removing sensitive data from a request data dict.
        Args:
            request_data: a dict containing a proposed user's data
        """
        request_data['payment_type'] = None
        request_data['password'] = None
        request_data['cc_number'] = None
        request_data['area_code'] = None
        request_data['sid'] = None
        return request_data


    async def _augment_sign_up_data(self, request_data, twilio_user):
        """A method for augmenting a new user record with Twilio 
        and other peripheral data. 
        Args:
            self: an instance of the UserManagement class
            request_data: a dict containing a proposed user's data
            twilio_user: a dict containing newly 
            created twilio subuser details
        """
        hashed_password = await generate_password_hash(request_data['password'])
        request_data['password'] = hashed_password  
        request_data['date_joined']: datetime.datetime.utcnow()
        request_data['sms_number']: twilio_user['sms_number']
        request_data['sid']: twilio_user['sid']
        return request_data


    async def signup(self):
        """A method for signing up for the service. 
        Args:
            self: an instance of the UserManagement class
        """
        # parse the request
        try:
            request_data = await self._parse_sign_up_request()
        except Exception as e:
            return 'There was a problem parsing your request.\
             Error message: {}'.format(str(e))

        # check that requested namespace is available
        user = await self.get_user(request_data['username'])
        if user:
            return 'Sorry, but that username is already taken.\
             Please choose a different username.'

        # create Twilio subaccount
        twilio = CreateTwilioAccount(friendly_name=username)
        try:
            twilio_user = await twilio.create_user_account()
        except:
            return 'Twilio error'

        # create system user and associate Twilio subaccount 
        request_data = self._augment_sign_up_data(request_data, twilio_user)
        user_id = await self.users_collection.insert(request_data)
        return_data = await self._strip_sensitive_fields(request_data)
        session['area_code'] = None
        return jsonify(return_data)


    async def login(self):
        """A method for logging in to the service.
        Args:
            self: an instance of the UserManagement class
        """
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
