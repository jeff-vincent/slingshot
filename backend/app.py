from quart import Quart
from motor.motor_asyncio import AsyncIOMotorClient
from config import mongo_uri


app = Quart(__name__)
client = AsyncIOMotorClient(mongo_uri)

users_collection = client.db.users


@app.route('/', methods=['GET'])
async def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug='true')