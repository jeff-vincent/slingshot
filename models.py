from config import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(10), unique=True, nullable=False)
    session_id = db.Column(db.Integer)
    def __repr__(self):
        return '<User %r>' % self.username

# class QA(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String(1000), unique=True, nullable=False)
#     correct_answer = db.Column(db.Integer)
#     submitted_answers = db.Column(db.Integer)

#     def __repr__(self):
#         return '<QA %r>' % self.question
