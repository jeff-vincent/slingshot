from flask import Flask, request, render_template
from twilio import twiml
import json

# Slingshot modules
import sms
import user

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

    print("<h2>Sign up Successful! Username: {} Password: {}</h2>".format(username, password))
    return '...'

def _login():
    # parse params
    username = request.form.get('username')
    password = request.form.get('password')

    # validate request

    # login
    with open('./users.txt', 'r') as users:
        for row in users:
            if username and password in row:
                with open('./active_users.txt', 'a') as active_users:
                    active_users.write(username + '\n')
            else:
                print('nah, suckah')
    return '...'
