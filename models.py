from config import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(10), unique=True, nullable=False)
    session_id = db.Column(db.Integer, unique=True)
    questions = db.relationship('Question', backref='author', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.username

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), unique=True, nullable=False)
    correct_answer = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answers = db.relationship('Answer', backref='author', lazy=True)
    def __repr__(self):
        return '<Question %r>' % self.id

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(1000), unique=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    def __repr__(self):
        return '<Answer %r>' % self.id