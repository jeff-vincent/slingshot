from config import app, db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.username