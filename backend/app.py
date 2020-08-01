from quart import Quart
from quart import request
from motor.motor_asyncio import AsyncIOMotorClient
from config import mongo_uri
from user_management import UserManagement

app = Quart(__name__)
client = AsyncIOMotorClient(mongo_uri)

users_collection = client.db.users
user_management = UserManagement()


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


if __name__ == '__main__':
    app.run(debug='true')
