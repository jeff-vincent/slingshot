from flask import Flask
from pymongo import Mongo

MONGO_URI = ''

app = Flask(__name__)
mongo = Mongo(MONGO_URI)


@app.route('/', methods=['GET'])
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug='true')