# db.py
from os import environ
from kafka import KafkaProducer
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = environ.get('MONGO_URI')


class KafkaPublish:

	def __init__(self):
		self.producer = KafkaProducer(bootstrap_servers='localhost:9092')


	async def write_to_users(self, write_dict):
		bytes_value = await bytes(json.dump(write_dict))
		producer.send('users', key=b'user', value=bytes_value)


	async def write_to_messages(self, write_dict):
		bytes_value = await bytes(json.dump(write_dict))
		producer.send('messages', key=b'message', value=bytes_value)


class MotorQuery:

	def __init__(self):
		self.client = AsyncIOMotorClient(MONGO_URI)

	async def get_user(self, username):
		user = await self.client.db.users_collection.find_one({'username': username})
		return user




