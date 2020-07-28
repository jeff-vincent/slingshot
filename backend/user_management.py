import asyncio
import datetime
from quart import session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


from twilio_account import CreateTwilioAccount


class UserManagement:

    def __init__(self, request, users_collection):
        self.request = request
        self.users_collection = users_collection

    async def signup(self):
        try:
            form = await self.request.form
            username = await form.get('username')
            password = await form.get('password')
            payment_type = await form.get('payment_type')
            cc_number = await form.get('cc_number')

        except Exception as e:
            return 'There was a problem parsing your request.\
             Error message: {}'.format(str(e))
        
        
        user = await self.users_collection.find_one({'username': username})
        
        if user:
            return 'Sorry, but that username is already taken.\
             Please choose a different username.'

        hashed_password = await generate_password_hash(password)
        twilio = CreateTwilioAccount(username)

        try:
            twilio_user = await twilio.create_user_account()
        except:
            return 'Twilio error'
        
        user_id = await self.users_collection.insert({'username': username,   
                                        'password': hashed_password,
                                        'date_joined': datetime.datetime.utcnow(),
                                        'sms_number': twilio_user['sms_number'],
                                        'sid': twilio_user['sid'], 
                                        'payment': {
                                        'type': payment_type,
                                        'cc_number': cc_number,
                                        'trial': True
                                        }})
        
        user = await self.users_collection.find_one({'username': username})
        data = {
            'username': user['username'],
            'date_joined': user['date_joined'],
            'sms_number': user['sms_number']
            }

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
            user = await self.users_collection.find_one({'username': username})
            
            if check_password_hash(user['password'],  password):
                sms_number = user['sms_number']
                sid = user['sid']
                session['sms_number'] = sms_number
                session['sid'] = sid
                return 'Logged in user: {}'.format(user['username'])
            
            return 'Please log in.'
        except Exception as e:
            return 'Login failed: ' + (str(e))

    async def recover_password(self):
        pass
