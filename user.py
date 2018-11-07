""" This is where user-related logic will live. """

from twilio.rest import Client
import slingshot_config

""" Create a subaccount """

def create_new_web_user(account_sid, auth_token):
    account_sid = account_sid
    auth_token = auth_token
    web_user = Client(account_sid, auth_token)
    return web_user
    
    
def get_web_user(user_storage, web_user_id):
    errors = []
    web_user = user_storage.web_user_id
    return web_user
