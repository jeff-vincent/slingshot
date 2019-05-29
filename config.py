from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static/dist', template_folder='templates/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Jeff:password@localhost/slingshotdb'

db = SQLAlchemy(app)
