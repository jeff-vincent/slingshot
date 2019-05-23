from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from twilio import twiml
from config import app, db
from models import User
import json

# Slingshot modules
import sms, user, models

def _handle_answer():
    #create answer_object
    answer_object = {}
    #parse data
    answer_object['data'] = request.form.get('Body')
    answer_object['sms_user'] = request.form.get('From')
    answer_object['web_user_id'] = request.form.get('To')

    print(answer_object)

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(answer_object.sms_user, answer_object.data))
    print(resp)
    return str(resp)

    # return '...'
    # #get associated web_user
    # web_user = user.get_web_user(answer_object.web_user_id)
    # #check if data should be stored
    # if web_user.store_data == True:
    #     web_user.current_session.current_question.answer_list.append(answer_object)
    # #thank the sms user for "weighing in"
    # return sms.auto_reply(request)

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
    
def _create_db_user(db):
    # parse params
    username = request.form.get('username')
    password = request.form.get('password')

    # Instantiate user object
    new_user = User(username=username, password=password)

    # Submit user object to db
    db.session.add(new_user)
    db.session.commit()

    # Confirm creation of new user in db
    confirmed_user = db.session.query(User).get(new_user.id)

    if confirmed_user:

        return 'Sign-up Successful. User ID:{}'.format(confirmed_user.id)

    return 'Well, that\'s awkward... Wanna try again?'

def _delete_db_user(db):
    # parse params
    username = request.form.get('username')
    password = request.form.get('password')

    # get user to be deleted
    delete_user = db.session.query(User).filter_by(username=username).first()

    # Validate
    if delete_user.password == password:

        # Delete User
        db.session.delete(delete_user)
        db.session.commit()

        return 'Deleted: {}'.format(delete_user)

    # If validation fails,  alert the user.
    return 'There was a problem authenticating your request.'

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

