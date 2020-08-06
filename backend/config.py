from os import environ

MONGO_URI = environ.get('MONGO_URI')

admin_sid = environ.get('ADMIN_SID')
auth_token = environ.get('AUTH_TOKEN')

twilio_available_sms_numbers_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{auth_token}/AvailablePhoneNumbers/US/Mobile.json?PageSize=1'

twilio_purchase_sms_number_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{auth_token}/IncomingPhoneNumbers.json'

twilio_send_sms_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{auth_token}/Messages.json'

twilio_create_subaccount_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts.json'

twilio_assign_new_number_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{admin_sid}/IncomingPhoneNumbers/{sms_number}.json'


