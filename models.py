from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    session_id = db.Column(db.Integer, unique=True,  nullable=True)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    questions = db.relationship('Question', backref='author', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.username

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), unique=True, nullable=False)
    correct_answer = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    closed = db.Column(db.Boolean, nullable=False)
    answers = db.relationship('Answer', backref='author', lazy=True)
    def __repr__(self):
        return '<Question %r>' % self.id

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(1000), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    to_number = db.Column(db.String(100), nullable=False)
    from_number = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Answer %r>' % self.id