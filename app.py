from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__, static_folder="static/dist", template_folder="static")

""" Requests from web_user """

@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')

@app.route('/sign-up', methods=['POST'])
def sign_up():
    return base_api._sign_up(request)

@app.route('/login', methods=['POST'])
def login():
    return base_api._login(request)

@app.route('/{member_id}', methods=['GET'])
def render_dashboard():
    # validate request
    if utils._is_valid_request(request) == True:
        return render_template('dashboard.html')
    else:
        return render_template('index.html')

@app.route('/{member_id}', methods=['POST'])
def update_dashboard():
    # validate request
    if utils._is_valid_request(request) == True:
        return base_api._update_dashboard(request)
    else:
        return render_template('index.html')

@app.route('/{member_id}/admin', methods=['GET'])
def render_admin():
    # validate request
    if utils._is_valid_request(request) == True:
        return render_template('admin.html')
    else:
        return render_template('index.html')

@app.route('/{member_id}/admin', methods=['POST'])
def update_admin():
    # validate request
    if utils._is_valid_request(request) == True:
        return base_api._update_admin(request)
    else:
        return render_template('index.html')

""" Requests from sms_user (Twilio) """

@app.route('/answer', methods=['POST'])
def handle_answer():
    return base_api._handle_answer(request)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
