from quart import Quart
from quart import request

from user_management import UserManagement
from sms import IncomingSMS

app = Quart(__name__)


@app.route('/', methods=['GET'])
async def index():
    return 'index'


@app.route('/sign-up', methods=['GET', 'POST'])
async def sign_up():
	if request.method == 'GET':
		return 'Sign up here.'
	elif request.method == 'POST':
		sign_up = await user_management.sign_up(request)
		return sign_up.json()
	else:
		return 'Error. Sign up here.'


@app.route('/login', methods=['GET', 'POST'])
async def login():
	if request.method == 'GET':
		return 'Login here.'
	elif request.method == 'POST':
		login = await user_management.login(request)
		return login.json()
	else:
		return 'Error. Sign up here.'


@app.route('/incoming-sms', methods=['POST'])
async def handle_incoming_sms():
	incoming_sms = IncomingSMS(request)
	handled_request = await incoming_sms.handle_sms_callback()
	return handled_request.json()


@app.route('/set-prompt', methods=['POST'])
# set time/datestamped prompt on user
async def set_prompt():
	pass


# TODO: @admin functionality
@app.route('/get-billable-users', methods=['GET'])
async def get_billable_users():
	pass



if __name__ == '__main__':
    app.run(debug='true')
