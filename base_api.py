from flask import Flask, request, render_template

# Slingshot modules
import sms
import user

def _handle_answer(request):
    #create answer_object
    answer_object = {}
    #parse data
    answer_object.data = flask.request.get('body')
    answer_object.sms_user = flask.request.get('from')
    answer_object.web_user_id = flask.request.get('to')
    #get associated web_user
    web_user = user.get_web_user(answer_object.web_user_id)
    #check if data should be stored
    if web_user.store_data == True:
        web_user.current_session.current_question.answer_list.append(answer_object)
    #thank the sms user for "weighing in"
    return sms.auto_reply(request)

def _sign_up(request):
    # parse params
    # validate request
    if user.good_signup_request(request):
        return web_user
    else:
        return render_template('index.html')

def _login(request):
    # parse params
    web_user_id = flask.request.get('email')
    web_user_password = flask.request.get('password')
    # retrieve web_user object
    web_user = user._get_web_user(web_user_id, web_user_password)
    # validate request
    if user._good_user(web_user) == True:
        return user._log_in_user(web_user)
    else:
        return render_template('index.html')
