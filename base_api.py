from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from twilio import twiml
from config import app, db
import random

# Slingshot modules
import sms, user
from models import User, Question, Answer

def _create_db_user(db):
    # parse params
    content = request.json
    username = content['username']
    password = content['password']
    phone_number = content['phone_number']
    
    session_id = random.randint(1000000000,2147483647)
    
    # Instantiate user object
    new_user = User(username=username, 
                    password=password, 
                    session_id=session_id, 
                    phone_number=phone_number)

    # Submit user object to db
    db.session.add(new_user)
    db.session.commit()

    # Confirm creation of new user in db
    confirmed_user = db.session.query(User).get(new_user.id)

    if confirmed_user:

        return 'Sign-up Successful. User ID:{}'.format(confirmed_user.id)

    return 'Well, that\'s awkward... Wanna try again?'

def _delete_db_user(db):
    # Parse params
    content = request.json
    username = content['username']
    password = content['password']

    # Get user to be deleted
    delete_user = db.session.query(User).filter_by(username=username).first()

    # Validate
    if delete_user.password == password:

        # Delete User
        db.session.delete(delete_user)
        db.session.commit()

        return 'Deleted: {}'.format(delete_user.username)

    # If validation fails,  alert the user.
    return 'There was a problem authenticating your request.'

def _login_db_user(db):
    # Parse params
    content = request.json
    username = content['username']
    password = content['password']
    
    # Get user to be logged in
    user = db.session.query(User).filter_by(username=username).first()

    # Authenticate
    if user.password and user.password == password:

        # Create Session ID
        session_id = random.randint(1000000000,2147483647)
        
        # Set Session ID on user object
        user.session_id = session_id

        # Submit user object to db
        db.session.commit()

        return str(session_id)

    # If auth fails, alert the user.
    return 'There was a problem authenticating your request.'

def _logout_db_user(db):
    # Parse params
    session_id = request.form.get('session_id')

    # Get user to be logged out. Using .first() on top of unique usernames 
    # for increased performance. 
    user = db.session.query(User).filter_by(session_id=session_id).first()

    # Reset Session ID to Falsy
    session_id = None
        
    # Update user's session ID in db
    user.session_id = session_id
    db.session.commit()

    return 'Logged out: {}'.format(user.username)

def _ask_question(db):
    # Parse params
    session_id = request.form.get('session_id')
    question = request.form.get('question')
    correct_answer = request.form.get('correct_answer')

    # Authenticate request
    if session_id:
    
        # Get user
        user = db.session.query(User).filter_by(session_id=session_id).first()

        if not user:
            return 'Please log in.'

        # Instantiate question object
        question = Question(question=question, user_id=user.id, correct_answer=correct_answer, closed=False)
        
        # Add question to db user object
        db.session.add(question)
        db.session.commit()

        return 'Question {} posed.'.format(question.id)
        
    return 'There was an error submitting your question.'

def _answer_question(db):
    # Parse params
    answer = request.form.get('answer')
    to_number = request.form.get('to_number')
    from_number = request.form.get('from_number')
    
    # Get user who asked question
    web_user = db.session.query(User).filter_by(phone_number=to_number).first()

    # Get last question web_user asked
    question = db.session.query(Question).filter_by(user_id=web_user.id).all()
    
    question_id = question[-1].id

    # Instantiate Answer object
    answer = Answer(answer=answer, to_number=to_number, from_number=from_number, question_id=question_id)

    # Add answer to db
    db.session.add(answer)
    db.session.commit()

    return 'Answer submitted.'



""" Write to local text file """
def _login():
    # parse params
    username = request.form.get('username')
    password = request.form.get('password')

    # validate
    with open('./users.txt', 'r') as users:
        for row in users:
            if username and password in row:
                # login
                with open('./active_users.txt', 'a') as active_users:
                    active_users.write(username + '\n')
                # report result
                return 'Login Successful'
    return 'Please Sign-up'

def _sign_up():
    # parse params
    username = request.form.get('username')
    password = request.form.get('password')

    # validate request

    # create new user
    with open ('./users.txt', 'a') as users:
        users.write(username + ' | ' + password + '\n')
    #confirm creation
    with open('./users.txt', 'r') as users:
        for row in users:
            if username and password in row:

                return 'Sign-up Successful'

    return 'Well, that\'s awkward... Wanna try again?'