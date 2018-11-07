""" This is where sms related logic will live """

from twilio.twiml.messaging_response import MessagingResponse


""" Send unbidden text message. ***Not currently being used***   """

def send_first(web_user, outgoing_message):
    client = web_user.twilio_client
    message = client.messages \
                .create(
                     body = outgoing_message.body,
                     from_ = outgoing_message.from_number,
                     to = outgoing_message.to_number
                 )

    print(message.sid)
    
""" Autoreply to incoming text messages (answers to questions posed). """    

def auto_reply(request):
    resp = MessagingResponse()
    resp.message('Thanks for weighing in!')
    return str(resp)
