admin_sid = ''
auth_token = ''
mongo_uri = ''

twilio_available_sms_numbers_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{auth_token}/AvailablePhoneNumbers/US/Mobile.json?PageSize=1'

twilio_purchase_sms_number_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{auth_token}/IncomingPhoneNumbers.json'

twilio_send_sms_base_uri = \
'https://api.twilio.com/2010-04-01/Accounts/{auth_token}/Messages.json'
