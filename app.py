from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from config import app, db
import base_api



""" Requests from web_user """

@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')

@app.route('/sign-up', methods=['POST'])
def sign_up(db):
    return base_api._sign_up()

@app.route('/login', methods=['POST'])
def login(db):
    return base_api._login()

@app.route('/user-status', methods=['POST'])
def get_user_status(db):
    logged_in = bool
    username = request.form.get('username')
    # check request's username against active_users
    with open('./active_users.txt', 'r') as active_users:
        for row in active_users:
            if username in row:
                logged_in = True
            else:
                logged_in = False
    # return user status
    if logged_in == True:
        return '{} is logged in.'.format(username)
    else:
        return '{} is not logged in.'.format(username)

@app.route('/{member_id}', methods=['POST'])
def update_dashboard():
    # validate request
    if utils._is_valid_request() == True:
        return base_api._update_dashboard()
    else:
        return render_template('index.html')

@app.route('/{member_id}/admin', methods=['GET'])
def render_admin():
    # validate request
    if utils._is_valid_request() == True:
        return render_template('admin.html')
    else:
        return render_template('index.html')

@app.route('/{member_id}/admin', methods=['POST'])
def update_admin():
    # validate request
    if utils._is_valid_request() == True:
        return base_api._update_admin(request)
    else:
        return render_template('index.html')

""" Requests from sms_user (Twilio) """

@app.route('/answer', methods=['POST'])
def handle_answer():
    return base_api._handle_answer()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
