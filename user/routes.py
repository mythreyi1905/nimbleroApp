from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup',methods=['POST'])
def signup():
    user = User()
    return user.signup()

@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login',methods=['POST'])
def login():
    return User().login()

@app.route('/user/sendMessage', methods=['POST'])
def sendMessage():
    return User().sendMessage()

@app.route('/user/readMessage', methods=['GET'])
def readMessage():
    user = User()
    return user.readMessage()


