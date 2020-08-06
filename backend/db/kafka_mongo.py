# kafka_mongo.py
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from backend.config import MONGO_URI

class KafkaMongo:

	def __init__(self):
		self.message_consumer = KafkaConsumer(
							    'message',
							     bootstrap_servers=['localhost:9092'],
							     auto_offset_reset='earliest',
							     enable_auto_commit=True,
							     group_id='my-group',
							     value_deserializer=lambda x: loads(x.decode('utf-8')))
		self.user_consumer = KafkaConsumer(
							    'user',
							     bootstrap_servers=['localhost:9092'],
							     auto_offset_reset='earliest',
							     enable_auto_commit=True,
							     group_id='my-group',
							     value_deserializer=lambda x: loads(x.decode('utf-8')))
		self.client = MongoClient(MONGO_URI)
		self.messages = self.client.db.messages
		self.users = self.client.db.users


	def run(self):
		"""A method to run the Kafka message and user consumers, and 
		to write the comsumed data to Mongo.
		Args:
			self: an instance of the KafkaMongo class
		"""
		while True:
			for message in self.message_consumer:
			    message = message.value
			    self.messages.insert_one(message)
			    print('{} added to {}'.format(message, messages))

			for user in self.user_consumer:
			    user = user.value
			    self.users.insert_one(user)
			    print('{} added to {}'.format(user, users))



if __name__ == '__main__':
	kafka_mongo = KafkaMongo()
	kafka_mongo.run()
	